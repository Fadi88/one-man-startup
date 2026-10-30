"""TPL-1 to TPL-5, TPL-41, TPL-42, TPL-122, TPL-123, TPL-57, TPL-76, TPL-97: the agents, skills and roster are well formed, wired up and small.

Agent and skill files with bad frontmatter are skipped silently by some tools,
so a broken file can vanish without anyone noticing. This check makes it loud.
"""
from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
import frontmatter  # noqa: E402

BUDGET = {"AGENTS.md": 9000, "agent": 5000, "skill": 5000}
TIERS = {"deep", "standard", "fast"}
ACCESS = {"read", "web", "run", "check", "edit", "delegate"}
RUNS_TOOL = re.compile(r"`python [^`]*tools/")
AGENT_KEYS = {"name", "description", "tier", "access", "skills", "hands_off_to"}

fails: list[str] = []


def fail(msg: str) -> None:
    fails.append(msg)
    print(f"FAIL  {msg}")


agent_files = sorted((ROOT / "agents").glob("*.md"))
skill_dirs = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
if not agent_files or not skill_dirs:
    fail("found no agents or no skills, a check over nothing is not a pass")
    sys.exit(1)

skills: dict[str, dict] = {}
for d in skill_dirs:
    f = d / "SKILL.md"
    if not f.exists():
        fail(f"TPL-3 skills/{d.name}/ has no SKILL.md")
        continue
    try:
        fm, body = frontmatter.read(f)
    except frontmatter.FrontmatterError as e:
        fail(f"TPL-3 {e}")
        continue
    if fm.get("name") != d.name:
        fail(f"TPL-3 skills/{d.name}/SKILL.md name is {fm.get('name')!r}, not the folder name")
    if len(str(fm.get("description", ""))) < 40:
        fail(f"TPL-3 skills/{d.name} description is missing or too short to say when to use it")
    if len(f.read_text(encoding="utf-8")) > BUDGET["skill"]:
        fail(f"TPL-5 skills/{d.name}/SKILL.md is over {BUDGET['skill']} characters, move detail to a sibling file")
    # TPL-76: a skill that only says "run that other skill" is a second name for one method.
    if len(body.strip()) < 400 and re.search(r"`skills/[a-z0-9-]+/`", body):
        fail(f"TPL-76 skills/{d.name}/SKILL.md only points at another skill; fold it into that skill")
    # TPL-57: each discipline skill ends with its excuses table and its red flags.
    if d.name in {"bug-fix", "verify-green", "requirement-first", "ordered-steps", "safe-data-write"}:
        if "| The excuse | The answer |" not in body or "Red flags:" not in body:
            fail(f"TPL-57 skills/{d.name}/SKILL.md lacks its excuses table or its 'Red flags:' line")
    skills[d.name] = fm

agents: dict[str, dict] = {}
for f in agent_files:
    try:
        fm, body = frontmatter.read(f)
    except frontmatter.FrontmatterError as e:
        fail(f"TPL-1 {e}")
        continue
    missing = AGENT_KEYS - fm.keys()
    if missing:
        fail(f"TPL-1 agents/{f.name} lacks {sorted(missing)}")
        continue
    if fm["name"] != f.stem:
        fail(f"TPL-1 agents/{f.name} name is {fm['name']!r}, not the file name")
    if fm["tier"] not in TIERS:
        fail(f"TPL-1 agents/{f.name} tier {fm['tier']!r} is not one of {sorted(TIERS)}")
    if not isinstance(fm["access"], list) or not set(fm["access"]) <= ACCESS or "read" not in fm["access"]:
        fail(f"TPL-1 agents/{f.name} access {fm['access']!r} must list read plus any of {sorted(ACCESS)}")
    elif "delegate" in fm["access"] and fm["name"] != "orchestrator":
        fail(f"TPL-1 agents/{f.name} has delegate; only the orchestrator delegates")
    if len(f.read_text(encoding="utf-8")) > BUDGET["agent"]:
        fail(f"TPL-5 agents/{f.name} is over {BUDGET['agent']} characters")
    agents[fm["name"]] = fm

for name, fm in agents.items():
    for s in fm["skills"]:
        if s not in skills:
            fail(f"TPL-2 agents/{name}.md lists skill {s!r}, which does not exist")
    told = [f"agents/{name}.md"] if RUNS_TOOL.search((ROOT / "agents" / f"{name}.md").read_text(encoding="utf-8")) else []
    told += [f"skills/{s}" for s in fm["skills"] if s in skills
             and RUNS_TOOL.search((ROOT / "skills" / s / "SKILL.md").read_text(encoding="utf-8"))]
    if told and not {"run", "check"} & set(fm["access"]):
        fail(f"TPL-42 agents/{name}.md is told to run a tool by {', '.join(told)} but has neither run nor check access")
    for a in fm["hands_off_to"]:
        if a not in agents:
            fail(f"TPL-2 agents/{name}.md hands off to {a!r}, which does not exist")

# A path to a skill's own file, named in any agent or skill, must exist (setup links its steps).
for f in [*(ROOT / "agents").glob("*.md"), *(ROOT / "skills").glob("*/*.md")]:
    for ref in re.findall(r"`(skills/[a-z0-9-]+/[A-Za-z0-9._-]+\.md)`", f.read_text(encoding="utf-8")):
        if not (ROOT / ref).exists():
            fail(f"TPL-3 {f.relative_to(ROOT).as_posix()} names {ref}, which does not exist")

# TPL-42: the check-only hook lets the checkers through and nothing else.
sys.path.insert(0, str(ROOT / "tools" / "lib"))
import check_only  # noqa: E402

for cmd, want in [("python tools/link_check.py docs/legal/regions/*.md", True),
                  ("python tools/run_all.py", True), ("py tools/checks/req_check.py --fix", True),
                  ("python tools/clean_template.py --yes", False), ("python tools/sync_adapters.py", False),
                  ("python tools/run_all.py && rm -rf docs", False), ("python tools/run_all.py > x", False),
                  ("echo $(whoami)", False), ("git push", False), ("", False),
                  ("python tools/render_mockups.py", True),
                  ("python tools/render_mockups.py docs/design/mockups/a.html", True),
                  ("python tools/render_mockups.py C:/Users/x/page.html", False),
                  ("python tools/render_mockups.py docs/design/mockups/../../x.html", False),
                  ("python tools/render_mockups.py && git push", False),
                  ("python tools/render_mockups.py --dark --rtl --text-scale 1.5", True),
                  ("python tools/render_mockups.py docs/design/mockups/a.html --text-scale 2", True),
                  ("python tools/render_mockups.py --text-scale 1.5; git push", False),
                  ("python tools/render_mockups.py --out C:/x", False),
                  ("python tools/render_mockups.py --text-scale", False),
                  ("python tools/link_check.py ../outside.md", False),
                  ("python tools/ab_size.py size --base 0.10 --target 0.12", True),
                  ("python tools/status_report.py", True), ("python tools/status_report.py --html", True),
                  ("python tools/status_report.py --html C:/Windows/x.html", False),
                  ("python tools/template_update.py", True),
                  ("python tools/template_update.py --apply AGENTS.md", False),
                  ("python tools/run_evals.py", False)]:
    if check_only.allowed(cmd) != want:
        fail(f"TPL-42 check_only {'blocks' if want else 'lets through'} {cmd!r}")

# TPL-122: every tool command a check-only agent's own file or skills tell it to run gets through
# the hook, so an instruction and the hook never contradict each other. Placeholders such as
# <files> stand for a plain argument.
for name, fm in agents.items():
    if "check" not in fm["access"] or "run" in fm["access"]:
        continue
    sources = [f"agents/{name}.md"] + [f"skills/{s}/SKILL.md" for s in fm["skills"] if s in skills]
    for src in sources:
        for cmd in re.findall(r"`((?:python3?|py) tools/[^`]+)`", (ROOT / src).read_text(encoding="utf-8")):
            plain = re.sub(r"<[^>]+>", "x", " ".join(cmd.split()))
            if not check_only.allowed(plain):
                fail(f"TPL-122 {src} tells {name} (check access) to run `{plain}`, which the hook blocks")

# TPL-97: the launch post drafts are never tracked.
import subprocess
tracked = subprocess.run(["git", "ls-files", "examples/template-launch/drafts", "examples/template-launch/replies.md"], cwd=ROOT,
                         capture_output=True, text=True).stdout.split()
if tracked:
    fail(f"TPL-97 launch drafts or replies are tracked by git: {', '.join(tracked)}; git rm --cached them")

agents_md = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
if len(agents_md) > BUDGET["AGENTS.md"]:
    fail(f"TPL-5 AGENTS.md is {len(agents_md)} characters, over its budget of {BUDGET['AGENTS.md']}")
team_md = (ROOT / "docs" / "TEAM.md").read_text(encoding="utf-8")
roster = set()
for shown, target in re.findall(r"^\| \[`([a-z0-9-]+)`\]\(\.\./agents/([a-z0-9-]+)\.md\) \|", team_md, flags=re.M):
    if shown != target:
        fail(f"TPL-4 docs/TEAM.md shows {shown!r} but links to agents/{target}.md")
    roster.add(shown)
for a in sorted(set(agents) - roster):
    fail(f"TPL-4 agent {a!r} is missing from the team table in docs/TEAM.md")
for a in sorted(roster - set(agents)):
    fail(f"TPL-4 docs/TEAM.md lists {a!r}, which has no file in agents/")

cfg = tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8"))
for a in cfg.get("team", {}).get("enabled", []):
    if a not in agents:
        fail(f"TPL-4 project.toml [team] enables {a!r}, which does not exist")
if cfg.get("owner", {}).get("level") not in {"non-technical", "basics", "technical"}:
    fail("TPL-28 project.toml [owner] level must be non-technical, basics or technical")
if cfg.get("product", {}).get("origin") not in {"unset", "new", "rebuild", "own"}:
    fail("TPL-41 project.toml [product] origin must be unset, new, rebuild or own")
if cfg.get("product", {}).get("origin") in {"rebuild", "own"} and not cfg["product"].get("based_on"):
    fail("TPL-41 project.toml [product] origin is rebuild or own but based_on does not name the app")
# TPL-43: nothing publishes or deploys until the founder has asked for it.
if cfg.get("publish", {}).get("enabled") is not True:
    for wf in sorted((ROOT / ".github" / "workflows").glob("*.y*ml")):
        if re.search(r"^\s*(pages: write|environment:|- uses: actions/deploy-pages)", wf.read_text(encoding="utf-8"), re.M):
            fail(f"TPL-43 .github/workflows/{wf.name} publishes or deploys, but project.toml [publish] enabled is not true")
if cfg.get("gates", {}).get("level") not in {"strict", "standard", "light"}:
    fail("TPL-4 project.toml [gates] level must be strict, standard or light")

# TPL-123: Claude Code asks the founder before the commands that delete, merge, publish or deploy
# (constitution rule 2). The project may add to the list, never drop one of these.
ASK = ["Bash(git push", "Bash(git merge", "Bash(git reset --hard", "Bash(rm -rf", "Bash(rm -fr", "Bash(rm -r",
       "Bash(git clean", "Bash(git branch -D", "Bash(gh pr merge", "Bash(gh release", "Bash(gh repo delete",
       "Bash(npm publish", "Bash(docker push", "Bash(vercel", "Bash(netlify deploy", "Bash(fly deploy",
       "Bash(firebase deploy", "Bash(supabase db push", "PowerShell(Remove-Item", "PowerShell(git push",
       "PowerShell(git merge", "PowerShell(git reset --hard", "PowerShell(git clean", "PowerShell(gh pr merge"]
settings = ROOT / ".claude" / "settings.json"
ask = json.loads(settings.read_text(encoding="utf-8")).get("permissions", {}).get("ask", []) if settings.exists() else []
for rule in ASK:
    if not any(a.startswith(rule + " ") or a.startswith(rule + ":") for a in ask):
        fail(f"TPL-123 .claude/settings.json does not ask before {rule[rule.index('(') + 1:]} commands")

if not fails:
    print(f"PASS  {len(agents)} agents and {len(skills)} skills are well formed, wired up and within budget")
sys.exit(1 if fails else 0)
