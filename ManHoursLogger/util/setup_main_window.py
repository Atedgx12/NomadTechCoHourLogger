import os

def setup_main_window():
    from util.imports import initialize_main_window, apply_window_styles, bg_color, set_icon, add_banner, create_main_content
    from util.imports import load_config, get_paths, precheck

    # Debug statement to indicate the start of setup
    print("Setting up the main window...")

    # Load configuration
    config = load_config()
    print("Loaded config:", config)

    # Get paths
    icon_path, banner_path, reports_path = get_paths(config)
    print(f"Icon path: {icon_path}")
    print(f"Banner path: {banner_path}")
    print(f"Reports path: {reports_path}")

    # Precheck reports path
    precheck(reports_path)
    print("Precheck completed for reports path.")

    # Initialize main window
    root = initialize_main_window()
    print("Initialized main window:", root)

    # Apply window styles
    apply_window_styles(root)
    print("Applied window styles.")

    # Set window icon
    icon_path_abs = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', icon_path))
    set_icon(root, icon_path_abs)
    print(f"Set window icon with path: {icon_path_abs}")

    # Add banner to window
    banner_path_abs = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', banner_path))
    add_banner(root, banner_path_abs, bg_color)
    print(f"Added banner with path: {banner_path_abs}")

    # Create main content frame
    main_frame = create_main_content(root, bg_color)
    print("Created main content frame:", main_frame)

    # Initialize projects and users lists
    projects = []  # Initialize your projects list
    users = []  # Initialize your users list if needed
    print("Initialized projects and users lists.")

    # Return all components
    return root, main_frame, reports_path, projects, users
