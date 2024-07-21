from tkinter import ttk
from .window_styles import entry_bg_color, fg_color

def apply_combobox_styles(combobox):
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground=entry_bg_color, background=entry_bg_color, foreground=fg_color)
    combobox.configure(style="TCombobox")
