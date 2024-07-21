def set_icon(root, icon_path):
    try:
        root.iconbitmap(icon_path)
        print(f"Loaded icon: {icon_path}")
    except Exception as e:
        print(f"Failed to load icon from {icon_path}: {e}")
