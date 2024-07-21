from .window_styles import bg_color, fg_color

def apply_label_styles(label):
    label.configure(bg=bg_color, fg=fg_color)
