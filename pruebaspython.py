import os
import sys

from pathlib import Path

cwd = Path.cwd()
print(cwd)

os.chdir("..")

print(cwd)
