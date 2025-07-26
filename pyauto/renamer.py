import os

def rename_files(folder, pattern, start=1):
    files = sorted(f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)))
    num = start
    renamed = []
    for f in files:
        ext = os.path.splitext(f)[1]
        new_name = pattern.replace("{num}", str(num)) + ext
        os.rename(os.path.join(folder, f), os.path.join(folder, new_name))
        renamed.append(new_name)
        num += 1
    return renamed
