"""TPL-30, TPL-20: cleaning a new project of the template's own content leaves it green.

Copies the repository to a scratch folder, fills project.toml as setup would, runs
tools/clean_template.py --yes there, and runs the full sweep on the result. Also checks that
the template's own content is really gone, so a clean that silently does nothing fails.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PY = sys.executable

fails = []
# TPL-20: a copy made from the template has no site until this clean removes pages.yml, so the
# landing page job must not run there (its first push would fail).
if "if: github.repository == 'Fadi88/one-man-startup'" not in (
        ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8"):
    fails.append("TPL-20 .github/workflows/pages.yml would also run, and fail, in a copy made from the template")

with tempfile.TemporaryDirectory() as tmp:
    copy = Path(tmp) / "project"
    shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__", "_site"))
    toml = copy / "project.toml"
    t = toml.read_text(encoding="utf-8")
    t = t.replace('[product]\nname = "unset"', '[product]\nname = "Example Product"', 1)
    t = t.replace('one_liner = "unset"', 'one_liner = "A sentence about what it does."', 1)
    toml.write_text(t, encoding="utf-8")

    def run(*args: str) -> subprocess.CompletedProcess:
        return subprocess.run([PY, *args], cwd=copy, capture_output=True, text=True, encoding="utf-8")

    r = run("tools/clean_template.py", "--yes")
    if r.returncode:
        fails.append(f"clean_template.py failed: {(r.stdout + r.stderr).strip()[-300:]}")
    run("tools/checks/req_check.py", "--fix")

    for gone in ["examples", "site", ".github/workflows/pages.yml", "tools/clean_template.py",
                 "tools/checks/clean_check.py"]:
        if (copy / gone).exists():
            fails.append(f"{gone} is still there after cleaning")
    for rel, pattern in [
        ("docs/requirements/p1-closed-decisions.md", r"About the template itself"),
        ("docs/requirements/p1-rejected.md", r"About the template itself"),
        ("docs/ASSUMPTIONS.md", r"^\| A-\d+ \|"),
        ("docs/EXPERIMENTS.md", r"^### \d+\."),
        ("docs/requirements/TPL.md", r"^\| TPL-(18|19|20|21|27|30|38) \|"),
        ("README.md", r"^# One-man startup"),
    ]:
        if re.search(pattern, (copy / rel).read_text(encoding="utf-8"), flags=re.M):
            fails.append(f"{rel} still matches {pattern!r} after cleaning")
    notice = copy / "docs" / "licenses" / "one-man-startup.txt"
    if not notice.exists() or "MIT License" not in notice.read_text(encoding="utf-8"):
        fails.append("the template's licence notice was not kept in docs/licenses/one-man-startup.txt")
    if "# Example Product" not in (copy / "README.md").read_text(encoding="utf-8"):
        fails.append("README.md was not rewritten for the project")

    # Every check on the cleaned copy. The style check is left out: it lists files through git,
    # which a scratch copy lacks, and it already runs on these same files in the main sweep.
    for chk in sorted((copy / "tools" / "checks").glob("*.py")):
        if chk.name == "style_check.py" or "NOT_A_CHECK" in chk.read_text(encoding="utf-8"):
            continue
        r = run(str(chk.relative_to(copy)))
        if r.returncode != 0:
            reds = [l for l in r.stdout.splitlines() if "FAIL" in l] or [r.stderr.strip()[-200:]]
            fails.append(f"{chk.name} is red on the cleaned copy: " + "; ".join(reds)[:300])

for f in fails:
    print(f"FAIL  TPL-30 {f}")
if not fails:
    print("PASS  a project cleaned of the template's own content is green")
sys.exit(1 if fails else 0)
