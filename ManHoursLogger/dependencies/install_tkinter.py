import subprocess
import sys

def install_tkinter():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tk"])

if __name__ == "__main__":
    install_tkinter()
