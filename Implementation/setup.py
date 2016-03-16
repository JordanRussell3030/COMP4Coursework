application_title = "Trigonometry Education Program"
main_python_file = "login_screen_window.py"

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32C"

includes = ["atexit", "re"]

setup(
        name = application_title,
        version = "0.1",
        description = "Sample cx_Freeze PyQt4 script",
        options = {"build.exe" : {"includes" : includes }},
        executables = [Executable(main_python_file, base)])
