import os

def get_current_user():
    return os.getlogin()

def ensure_reports_folder_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_project_folder(base_path, project_name):
    project_path = os.path.join(base_path, project_name)
    ensure_reports_folder_exists(project_path)
    return project_path
