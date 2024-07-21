import tkinter as tk
import sys
import os
from init.setup_buttons import setup_buttons

# Add necessary directories to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'styles')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'init')))

# Import modules
from styles.apply_window_styles import apply_window_styles, bg_color
from styles.apply_combobox_styles import apply_combobox_styles
from init.load_config import load_config
from init.get_paths import get_paths
from init.precheck import precheck
from init.initialize_main_window import initialize_main_window
from init.set_icon import set_icon
from init.add_banner import add_banner
from init.create_main_content import create_main_content
from init.setup_labels_entries import setup_labels_entries
from init.setup_combobox import setup_combobox
from init.setup_buttons import setup_buttons
from lib.create_project_folder import create_project_folder
from lib.generate_report import generate_report
from lib.get_current_user import get_current_user
from PIL import Image, ImageTk  # Add Pillow imports here
