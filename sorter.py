import os
import shutil
from .config import FILE_TYPES
from .utils import create_folder

def sort_files(download_folder="Downloads"):
    folder_path = os.path.expanduser(f"~/{download_folder}")
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1].lower()
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    dest_folder = os.path.join(folder_path, category)
                    create_folder(dest_folder)
                    shutil.move(filepath, os.path.join(dest_folder, filename))
                    print(f"Moved: {filename} ➜ {category}")
                    break
