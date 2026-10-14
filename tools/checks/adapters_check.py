"""TPL-6: the generated tool files match their sources."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
r = subprocess.run([sys.executable, str(ROOT / "tools" / "sync_adapters.py"), "--check"],
                   cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
print(r.stdout + r.stderr, end="")
sys.exit(r.returncode)
