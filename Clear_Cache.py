import os
import shutil

# Clear files in the specific temp folder
temp_folder = r"C:\Users\ntoma\AppData\Local\Temp"
for filename in os.listdir(temp_folder):
    file_path = os.path.join(temp_folder, filename)
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except PermissionError as e:
        print(f"Unable to delete {e}")
