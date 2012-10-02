import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "tablewriter",
        version = "0.3.6",
        description = "Write HTML tables from CSV files.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("tablewriter.py", base=base)])