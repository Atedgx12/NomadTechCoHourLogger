import sys
import os
import tkinter as tk

# Add the directory containing 'lib' to the system path
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
if lib_path not in sys.path:
    sys.path.append(lib_path)
    print(f"Added lib directory to sys.path: {lib_path}")

# Add the user site-packages directory to the system path
user_site_packages = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Python', 'Python39', 'site-packages')
if user_site_packages not in sys.path:
    sys.path.append(user_site_packages)
    print(f"Added user site-packages to sys.path: {user_site_packages}")

# Add the root directory and dependencies directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dependencies')))
print(f"Added directories to sys.path: {sys.path}")

# Check and install dependencies
from check_and_install_dependencies import check_and_install_dependencies
print("Checking and installing dependencies...")
check_and_install_dependencies()
print("Dependencies checked and installed.")

# Import necessary modules
from util.setup_main_window import setup_main_window
from util.setup_entries import setup_labels_entries
from util.setup_buttons import setup_buttons
from lib.create_project_folder import create_project_folder
from lib.generate_report import generate_report
from lib.get_current_user import get_current_user
from lib.add_user import load_users
from lib.add_project import load_projects

print("Modules imported successfully.")

# Load users and projects from files
users = load_users()
projects = load_projects()

# Initialize the main window and main content frame
print("Initializing the main window and main content frame...")
root, main_frame, reports_path, _, _ = setup_main_window()
print(f"Main window initialized: {root}")
print(f"Main frame created: {main_frame}")
print(f"Reports path: {reports_path}")

# Setup labels, entries, and combobox
print("Setting up labels, entries, and combobox...")
user_dropdown, project_label, project_dropdown = setup_labels_entries(main_frame)
project_dropdown['values'] = projects
user_dropdown['values'] = users
print("Labels, entries, and combobox setup completed.")
print(f"user_dropdown: {user_dropdown}")
print(f"project_label: {project_label}")
print(f"project_dropdown: {project_dropdown}")

# Debug statements before calling setup_buttons
print("Calling setup_buttons with arguments:")
print(f"main_frame: {main_frame}")
print(f"project_dropdown: {project_dropdown}")
print(f"root: {root}")
print(f"projects: {projects}")
print(f"reports_path: {reports_path}")
print(f"users: {users}")
print(f"user_dropdown: {user_dropdown}")
print(f"create_project_folder: {create_project_folder}")
print(f"generate_report: {generate_report}")
print(f"get_current_user: {get_current_user}")

# Setup buttons with correct arguments
print("Setting up buttons...")
setup_buttons(
    main_frame=main_frame,               # tk.Frame
    project_dropdown=project_dropdown,   # tk.Combobox
    root=root,                           # tk.Tk
    projects=projects,                   # List of projects
    reports_path=reports_path,           # String path
    users=users,                         # List of users
    user_dropdown=user_dropdown,         # tk.Combobox
    create_project_folder=create_project_folder,    # Function reference
    generate_report=generate_report,     # Function reference
    get_current_user=get_current_user    # Function reference
)
print("Buttons setup completed.")

# Start the main loop
print("Starting the main loop...")
root.mainloop()
print("Main loop exited.")
