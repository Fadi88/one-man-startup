"""TPL-1 to TPL-5: the agents, skills and roster are well formed, wired up and small.

Agent and skill files with bad frontmatter are skipped silently by some tools,
so a broken file can vanish without anyone noticing. This check makes it loud.
"""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "lib"))
import frontmatter  # noqa: E402

BUDGET = {"AGENTS.md": 9000, "agent": 5000, "skill": 5000}
TIERS = {"deep", "standard", "fast"}
ACCESS = {"read", "web", "run", "edit", "delegate"}
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
    for a in fm["hands_off_to"]:
        if a not in agents:
            fail(f"TPL-2 agents/{name}.md hands off to {a!r}, which does not exist")

# A path to a skill's own file, named in any agent or skill, must exist (setup links its steps).
for f in [*(ROOT / "agents").glob("*.md"), *(ROOT / "skills").glob("*/*.md")]:
    for ref in re.findall(r"`(skills/[a-z0-9-]+/[A-Za-z0-9._-]+\.md)`", f.read_text(encoding="utf-8")):
        if not (ROOT / ref).exists():
            fail(f"TPL-3 {f.relative_to(ROOT).as_posix()} names {ref}, which does not exist")

agents_md = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
if len(agents_md) > BUDGET["AGENTS.md"]:
    fail(f"TPL-5 AGENTS.md is {len(agents_md)} characters, over its budget of {BUDGET['AGENTS.md']}")
roster = set()
for shown, target in re.findall(r"^\| \[`([a-z0-9-]+)`\]\(agents/([a-z0-9-]+)\.md\) \|", agents_md, flags=re.M):
    if shown != target:
        fail(f"TPL-4 AGENTS.md shows {shown!r} but links to agents/{target}.md")
    roster.add(shown)
for a in sorted(set(agents) - roster):
    fail(f"TPL-4 agent {a!r} is missing from the team table in AGENTS.md")
for a in sorted(roster - set(agents)):
    fail(f"TPL-4 AGENTS.md lists {a!r}, which has no file in agents/")

cfg = tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8"))
for a in cfg.get("team", {}).get("enabled", []):
    if a not in agents:
        fail(f"TPL-4 project.toml [team] enables {a!r}, which does not exist")
if cfg.get("owner", {}).get("level") not in {"non-technical", "basics", "technical"}:
    fail("TPL-28 project.toml [owner] level must be non-technical, basics or technical")
if cfg.get("gates", {}).get("level") not in {"strict", "standard", "light"}:
    fail("TPL-4 project.toml [gates] level must be strict, standard or light")

if not fails:
    print(f"PASS  {len(agents)} agents and {len(skills)} skills are well formed, wired up and within budget")
sys.exit(1 if fails else 0)
