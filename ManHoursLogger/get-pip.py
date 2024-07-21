#! /usr/bin/env python
# This is a pip bootstrap script to install pip.
import os
import sys
import urllib.request
import tarfile

def download_file(url, filename):
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        out_file.write(response.read())

def install_pip():
    tarball_url = 'https://files.pythonhosted.org/packages/source/p/pip/pip-21.3.1.tar.gz'
    tarball_filename = 'pip-21.3.1.tar.gz'
    extract_dir = 'pip-21.3.1'

    print(f"Downloading pip from {tarball_url}")
    download_file(tarball_url, tarball_filename)

    print(f"Extracting {tarball_filename}")
    with tarfile.open(tarball_filename) as tar:
        tar.extractall()

    print(f"Installing pip from {extract_dir}")
    os.system(f"{sys.executable} {extract_dir}/setup.py install")

if __name__ == "__main__":
    install_pip()
