"""TPL-112: the numbers an A/B test needs, computed once, never typed by hand.

    python tools/ab_size.py size --base 0.10 --target 0.12        users needed per arm
    python tools/ab_size.py srm --a 5120 --b 4880                 is the split what was planned?
    python tools/ab_size.py read --a-users 4000 --a-hits 400 --b-users 4000 --b-hits 480

`size` is the standard sample size for comparing two proportions (two-sided, unpooled
variance): n = (z(1-alpha/2) + z(power))^2 * (p1(1-p1) + p2(1-p2)) / (p1 - p2)^2, rounded up.
`srm` is the sample ratio mismatch test: a chi-square on the arm counts against the planned
split; p under 0.001 means assignment is broken and the result is void. `read` is the two-
proportion z-test on the result, read once, at the planned size. Standard library only.
"""
from __future__ import annotations

import argparse
import math
import sys
from statistics import NormalDist

Z = NormalDist()


def size(base: float, target: float, alpha: float = 0.05, power: float = 0.8) -> int:
    """Users needed in each arm to tell `base` from `target`."""
    if not (0 < base < 1 and 0 < target < 1) or base == target:
        raise ValueError("base and target must differ and lie between 0 and 1")
    z = Z.inv_cdf(1 - alpha / 2) + Z.inv_cdf(power)
    var = base * (1 - base) + target * (1 - target)
    return math.ceil(z * z * var / (base - target) ** 2)


def srm(a: int, b: int, share_a: float = 0.5) -> float:
    """p-value that counts a and b came from the planned split (chi-square, one degree of freedom)."""
    n = a + b
    ea, eb = n * share_a, n * (1 - share_a)
    chi2 = (a - ea) ** 2 / ea + (b - eb) ** 2 / eb
    return math.erfc(math.sqrt(chi2 / 2))


def read(a_users: int, a_hits: int, b_users: int, b_hits: int) -> tuple[float, float, float]:
    """Rates of A and B, and the two-sided p-value of the difference (pooled z-test)."""
    pa, pb = a_hits / a_users, b_hits / b_users
    pool = (a_hits + b_hits) / (a_users + b_users)
    se = math.sqrt(pool * (1 - pool) * (1 / a_users + 1 / b_users))
    p = 2 * (1 - Z.cdf(abs(pb - pa) / se)) if se else 1.0
    return pa, pb, p


# Worked by hand from the formulas above, so a change to the code that moves them is caught.
# size(0.10, 0.12): z = 1.959964 + 0.841621 = 2.801585, z^2 = 7.848879, var = 0.09 + 0.1056 =
# 0.1956, 7.848879 * 0.1956 / 0.0004 = 3838.1 -> 3839.
# srm(5000, 5000) = 1.0; srm(5200, 4800): chi2 = 16, erfc(sqrt(8)) = 6.3e-5.
SAMPLES = [
    (lambda: size(0.10, 0.12), 3839),
    (lambda: round(srm(5000, 5000), 6), 1.0),
    (lambda: srm(5200, 4800) < 0.001, True),
    (lambda: srm(5050, 4950) > 0.001, True),
    (lambda: read(1000, 100, 1000, 100)[2], 1.0),
]


def selftest() -> list[str]:
    fails = []
    for i, (f, want) in enumerate(SAMPLES):
        got = f()
        if got != want:
            fails.append(f"FAIL  TPL-112 self-test sample {i}: got {got}, wanted {want}")
    return fails


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("size")
    s.add_argument("--base", type=float, required=True, help="today's rate, e.g. 0.10")
    s.add_argument("--target", type=float, required=True, help="the smallest rate worth acting on")
    s.add_argument("--alpha", type=float, default=0.05)
    s.add_argument("--power", type=float, default=0.8)
    m = sub.add_parser("srm")
    m.add_argument("--a", type=int, required=True)
    m.add_argument("--b", type=int, required=True)
    m.add_argument("--share-a", type=float, default=0.5)
    r = sub.add_parser("read")
    for k in ("a-users", "a-hits", "b-users", "b-hits"):
        r.add_argument(f"--{k}", type=int, required=True)
    sub.add_parser("selftest")
    a = ap.parse_args()
    if a.cmd == "size":
        n = size(a.base, a.target, a.alpha, a.power)
        print(f"{n} users per arm, {2 * n} in all (base {a.base}, target {a.target}, "
              f"alpha {a.alpha}, power {a.power})")
    elif a.cmd == "srm":
        p = srm(a.a, a.b, a.share_a)
        print(f"p = {p:.6f}: " + ("SAMPLE RATIO MISMATCH, assignment is broken, the result is void"
                                  if p < 0.001 else "split as planned"))
        return 1 if p < 0.001 else 0
    elif a.cmd == "read":
        pa, pb, p = read(a.a_users, a.a_hits, a.b_users, a.b_hits)
        print(f"A {pa:.4f}, B {pb:.4f}, difference {pb - pa:+.4f}, p = {p:.4f}")
    else:
        fails = selftest()
        print("\n".join(fails) or f"PASS  TPL-112 {len(SAMPLES)} worked samples")
        return 1 if fails else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
