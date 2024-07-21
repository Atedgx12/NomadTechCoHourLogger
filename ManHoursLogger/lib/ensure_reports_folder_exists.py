import os

def ensure_reports_folder_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
