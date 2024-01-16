import os

def empty_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Iterate over the files and remove themP
    for file in files:
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                # If you want to empty subfolders as well, you can recursively call the function
                empty_folder(file_path)
        except Exception as e:
            print(f"Error: {e}")
