import os

def get_paths(config):
    icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', config.get("icon_path", "../icons/icon.ico")))
    banner_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', config.get("banner_path", "../icons/banner.bmp")))
    reports_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', config.get("reports_path", "../reports")))
    return icon_path, banner_path, reports_path
