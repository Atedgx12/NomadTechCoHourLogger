import tkinter as tk
from tkinter import simpledialog
import json
import os

def add_project(root, projects, project_dropdown, create_project_folder, reports_path):
    print("Prompting user to enter project name...")
    project_name = simpledialog.askstring("Add Project", "Enter project name:", parent=root)
    
    if project_name:
        print(f"User entered project name: {project_name}")
        
        projects.append(project_name)
        print("Updated projects list:", projects)
        project_dropdown['values'] = projects
        print("Updated project_dropdown values:", project_dropdown['values'])
        
        create_project_folder(reports_path, project_name)
        save_projects(projects)
        print("Projects list saved successfully.")
    else:
        print("No project name entered.")

def save_projects(projects):
    projects_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'files', 'projects.json'))
    print(f"Saving projects to file: {projects_file_path}")
    
    with open(projects_file_path, 'w') as file:
        json.dump(projects, file)
    print("Projects list saved to file.")

def load_projects():
    projects_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'files', 'projects.json'))
    
    if os.path.exists(projects_file_path):
        print(f"Loading projects from file: {projects_file_path}")
        with open(projects_file_path, 'r') as file:
            projects = json.load(file)
        print("Projects loaded successfully.")
        return projects
    else:
        print("Projects file does not exist.")
        return []
