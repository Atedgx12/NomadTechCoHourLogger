import tkinter as tk
from tkinter import ttk

def setup_labels_entries(main_frame):
    print("Setting up labels and entries...")

    # Create user_project_frame
    user_project_frame = tk.Frame(main_frame, bg=main_frame['bg'])
    user_project_frame.pack(fill="x", pady=10)
    print("Created user_project_frame:", user_project_frame)
    print("Background color:", main_frame['bg'])

    # Create user_label
    user_label = tk.Label(user_project_frame, text="User:", bg=main_frame['bg'], fg="#ffffff")
    user_label.pack(side="left", padx=5)
    print("Created user_label:", user_label)
    print("Label text:", user_label.cget('text'))
    print("Label background color:", user_label.cget('bg'))
    print("Label foreground color:", user_label.cget('fg'))

    # Create user_dropdown
    user_dropdown = ttk.Combobox(user_project_frame)
    user_dropdown.pack(side="left", padx=5)
    print("Created user_dropdown:", user_dropdown)
    print("Dropdown current value:", user_dropdown.get())

    # Create project_label
    project_label = tk.Label(user_project_frame, text="Project:", bg=main_frame['bg'], fg="#ffffff")
    project_label.pack(side="left", padx=5)
    print("Created project_label:", project_label)
    print("Label text:", project_label.cget('text'))
    print("Label background color:", project_label.cget('bg'))
    print("Label foreground color:", project_label.cget('fg'))

    # Create project_dropdown
    project_dropdown = ttk.Combobox(user_project_frame)
    project_dropdown.pack(side="left", padx=5)
    print("Created project_dropdown:", project_dropdown)
    print("Dropdown current value:", project_dropdown.get())

    return user_dropdown, project_label, project_dropdown
