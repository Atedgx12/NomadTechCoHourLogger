import tkinter as tk
from tkinter import ttk

bg_color = "#2e2e2e"
fg_color = "#ffffff"
btn_color = "#444444"
entry_bg_color = "#3e3e3e"

def apply_styles(widget):
    widget.configure(bg=bg_color, fg=fg_color)
    if isinstance(widget, tk.Button):
        widget.configure(bg=btn_color, fg=fg_color)
    elif isinstance(widget, tk.Entry):
        widget.configure(bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
    elif isinstance(widget, ttk.Combobox):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground=entry_bg_color, background=entry_bg_color, foreground=fg_color)

def apply_window_styles(window):
    window.configure(bg=bg_color)
