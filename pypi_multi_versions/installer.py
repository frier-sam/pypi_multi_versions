import subprocess
import sys
import os

def install_version(package_name, version, path):
    """
    Installs a specific version of a package into the specified directory.
    """
    try:
        full_package_name = f"{package_name}=={version}"
        target_path = os.path.join(path, package_name, version)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        subprocess.check_call([sys.executable, "-m", "pip", "install", full_package_name, "--target={}".format(target_path)])
    except subprocess.CalledProcessError as e:
        print(f"Installation failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
