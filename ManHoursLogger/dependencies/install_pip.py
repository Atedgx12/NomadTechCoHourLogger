import subprocess
import sys
import os

def install_pip():
    print("pip not found. Installing pip...")
    get_pip_path = os.path.join(os.path.dirname(__file__), 'get-pip.py')
    subprocess.check_call([sys.executable, get_pip_path])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    print("pip installed.")

if __name__ == "__main__":
    install_pip()
