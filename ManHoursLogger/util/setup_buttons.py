import tkinter as tk
from tkinter import messagebox
from start_work import start_work
from stop_work import stop_work
from add_user import add_user
from add_project import add_project

def on_create_project(project_dropdown, create_project_folder, projects):
    project_name = project_dropdown.get()
    if not project_name:
        messagebox.showwarning("Input Error", "Please enter a project name.")
        return
    if project_name in projects:
        messagebox.showwarning("Duplicate Project", f"Project '{project_name}' already exists.")
        return
    create_project_folder(project_name)
    projects.append(project_name)
    project_dropdown['values'] = projects
    messagebox.showinfo("Success", f"Project '{project_name}' created successfully.")

def on_generate_report(project_dropdown, user_dropdown, generate_report, reports_path):
    project_name = project_dropdown.get()
    user_name = user_dropdown.get()
    if not project_name or not user_name:
        messagebox.showwarning("Input Error", "Please select both a project and a user.")
        return
    report_path = generate_report(project_name, user_name, reports_path)
    messagebox.showinfo("Report Generated", f"Report generated at {report_path}")

def setup_buttons(main_frame, project_dropdown, root, projects, reports_path, users, user_dropdown, create_project_folder, generate_report, get_current_user):
    # Debug statements
    print("setup_buttons called with arguments:")
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

    button_frame = tk.Frame(main_frame, bg=main_frame['bg'])
    button_frame.pack(pady=10)

    start_time = None

    def start_work_button():
        nonlocal start_time
        start_time = start_work()

    def stop_work_button():
        project_name = project_dropdown.get()
        stop_work(start_time, generate_report, get_current_user, project_name, reports_path, create_project_folder)

    start_button = tk.Button(button_frame, text="Start Work", command=start_work_button)
    start_button.pack(side="left", padx=5)

    stop_button = tk.Button(button_frame, text="Stop Work", command=stop_work_button)
    stop_button.pack(side="left", padx=5)

    add_project_button = tk.Button(button_frame, text="Add Project", command=lambda: add_project(root, projects, project_dropdown, create_project_folder, reports_path))
    add_project_button.pack(side="left", padx=5)

    add_user_button = tk.Button(button_frame, text="Add User", command=lambda: add_user(root, users, user_dropdown))
    add_user_button.pack(side="left", padx=5)
