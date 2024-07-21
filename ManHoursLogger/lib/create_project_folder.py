from .ensure_reports_folder_exists import ensure_reports_folder_exists
import os

def create_project_folder(base_path, project_name):
    print(f"Creating project folder with base path: {base_path} and project name: {project_name}")

    # Combine base_path and project_name to get the full project path
    project_path = os.path.join(base_path, project_name)
    print(f"Constructed project path: {project_path}")

    # Ensure that the reports folder exists
    print(f"Ensuring reports folder exists at: {project_path}")
    ensure_reports_folder_exists(project_path)
    print(f"Reports folder confirmed or created at: {project_path}")

    return project_path
