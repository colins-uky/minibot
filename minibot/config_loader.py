import yaml
import os
from ament_index_python.packages import get_package_share_directory


def return_config():
    cfg = None

    filepath = get_package_share_directory("minibot").replace("/install/minibot/share/minibot", "")
    
    new_path = os.path.join(filepath, "src", "minibot", "config.yaml")

    with open(new_path, 'r') as file:
        cfg = yaml.load(file, Loader=yaml.SafeLoader)

    return cfg

def return_pkg_path():
    ws_path = get_package_share_directory("minibot").replace("/install/minibot/share/minibot", "")

    pkg_path = os.path.join(ws_path, "src", "minibot")

    return pkg_path