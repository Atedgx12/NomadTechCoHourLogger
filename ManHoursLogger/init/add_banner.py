import tkinter as tk
from PIL import Image, ImageTk
from styles.auto_resize import resize_image

def add_banner(root, banner_path, bg_color):
    try:
        banner_label = tk.Label(root, bg=bg_color)
        banner_label.pack(side="top", fill="x", pady=10)
        
        def update_banner():
            window_width = root.winfo_width()
            banner_image = resize_image(banner_path, window_width)
            banner_label.config(image=banner_image)
            banner_label.image = banner_image  # Keep a reference to avoid garbage collection

        root.bind('<Configure>', lambda event: update_banner())
        update_banner()
        print(f"Loaded banner: {banner_path}")
    except Exception as e:
        print(f"Failed to load banner from {banner_path}: {e}")
        banner_label = tk.Label(root, text="Man Hours Logger", bg=bg_color, fg="#ffffff", font=("Helvetica", 24, "bold"))
        banner_label.pack(side="top", fill="x", pady=10)
    return banner_label
