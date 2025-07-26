import shutil
import os
from datetime import datetime

def backup_folder(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = os.path.basename(src.rstrip("/")) + "_" + timestamp
    backup_path = os.path.join(dest, backup_name)
    shutil.copytree(src, backup_path)
    return backup_path
