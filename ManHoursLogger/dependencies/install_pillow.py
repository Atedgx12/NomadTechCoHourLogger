import subprocess
import sys

def install_pillow():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])

if __name__ == "__main__":
    install_pillow()
