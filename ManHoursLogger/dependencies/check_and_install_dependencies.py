import subprocess
import sys
import os

def install_package(package_name):
    print(f"Attempting to install package: {package_name}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    print(f"Package {package_name} installed successfully.")

def check_and_install_dependencies():
    # Ensure pip is installed
    print("Checking if pip is installed...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
        print("Pip is already installed.")
    except subprocess.CalledProcessError:
        print("Pip is not installed. Attempting to install pip...")
        try:
            from install_pip import install_pip
            install_pip()
            print("Pip installed successfully.")
        except subprocess.CalledProcessError:
            print("Failed to install pip. Please install pip manually using the following steps:")
            print("1. Navigate to the 'dependencies' folder.")
            print("2. Run the command: python get-pip.py")
            sys.exit(1)

    # List of dependencies and their import names
    dependencies = {
        "Pillow": "PIL",
        # Add other dependencies as needed
    }

    for package, import_name in dependencies.items():
        print(f"Checking for package: {package}")
        try:
            __import__(import_name)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"{package} not found. Installing...")
            install_package(package)
            print(f"{package} installed.")

if __name__ == "__main__":
    check_and_install_dependencies()
