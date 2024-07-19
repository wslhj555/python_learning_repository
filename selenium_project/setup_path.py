import sys
import os


def setup_path():
    project_root = os.path.abspath(os.path.dirname(__file__))
    if project_root not in sys.path:
        sys.path.append(project_root)
