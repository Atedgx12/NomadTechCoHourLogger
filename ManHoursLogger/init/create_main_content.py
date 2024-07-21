import tkinter as tk

def create_main_content(root, bg_color):
    main_frame = tk.Frame(root, bg=bg_color)
    main_frame.pack(expand=True, fill="both")
    return main_frame
