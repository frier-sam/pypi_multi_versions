import os
import sys
from contextlib import contextmanager

@contextmanager
def import_helper(package_name, version, path):
    """
    Context manager to temporarily add a package version to sys.path.
    """
    package_path = os.path.abspath(os.path.join(path, package_name, version))
    if not os.path.exists(package_path):
        raise ImportError(f"Package path {package_path} does not exist. please install the package first")

    original_sys_path = sys.path.copy()
    sys.path.insert(1, package_path)
    

    try:
        yield
    finally:
        sys.path = original_sys_path
