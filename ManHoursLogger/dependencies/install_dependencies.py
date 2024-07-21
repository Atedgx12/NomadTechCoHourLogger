import subprocess
import sys
import os

def run_install_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    subprocess.check_call([sys.executable, script_path])

def install_all():
    dependencies = [
        "install_pillow.py",
        "install_tkinter.py"  # Add other installation scripts as needed
    ]
    for dependency in dependencies:
        run_install_script(dependency)

if __name__ == "__main__":
    install_all()
