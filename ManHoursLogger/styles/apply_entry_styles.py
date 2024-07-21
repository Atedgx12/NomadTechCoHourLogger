from .window_styles import entry_bg_color, fg_color

def apply_entry_styles(entry):
    entry.configure(bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
