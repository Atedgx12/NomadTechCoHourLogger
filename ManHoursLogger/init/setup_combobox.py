from tkinter import ttk
from styles.apply_combobox_styles import apply_combobox_styles

def setup_combobox(main_frame):
    project_dropdown = ttk.Combobox(main_frame)
    apply_combobox_styles(project_dropdown)
    project_dropdown.pack()
    return project_dropdown
