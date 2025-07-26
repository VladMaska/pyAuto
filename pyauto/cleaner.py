import os
import glob

def clean_folder(folder, extensions):
    deleted_files = []
    for ext in extensions:
        pattern = os.path.join(folder, f"*.{ext}")
        for f in glob.glob(pattern):
            os.remove(f)
            deleted_files.append(f)
    return deleted_files
