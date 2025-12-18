import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

# Prepend src to sys.path so tests import the local package
sys.path.insert(0, str(SRC))

# Ensure local CLI wrapper is on PATH for subprocess calls
os.environ["PATH"] = str(ROOT) + os.pathsep + os.environ.get("PATH", "")
