"""TPL-8: no banned characters (project.toml [style] banned_chars) in any tracked text file.

A style rule that is only written down drifts; this makes it a check. Reports
every hit with its line so the fix is mechanical.
"""
from __future__ import annotations

import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXT = {".md", ".py", ".toml", ".json", ".yml", ".yaml", ".txt", ".js", ".ts", ".tsx", ".jsx",
        ".css", ".html", ".svg", ".kt", ".swift", ".go", ".rs", ".sql", ".sh", ".mdc", ""}

cfg = tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8"))
banned = cfg.get("style", {}).get("banned_chars", [])

listed = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=ROOT,
                        capture_output=True, text=True).stdout.splitlines()
files = [ROOT / f for f in listed if Path(f).suffix in TEXT and (ROOT / f).is_file()]
if not files:
    print("FAIL  found no files to read, a style check over nothing is not a pass")
    sys.exit(1)

hits = 0
for f in files:
    try:
        lines = f.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        continue
    for n, line in enumerate(lines, 1):
        for ch in banned:
            if ch in line:
                print(f"FAIL  {f.relative_to(ROOT)}:{n} has U+{ord(ch):04X}")
                hits += 1
print(f"PASS  read {len(files)} files for {len(banned)} banned characters" if not hits else "")
sys.exit(1 if hits else 0)
