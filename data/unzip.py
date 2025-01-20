import os
import zipfile

def unzip_files_in_directory(directory):
    """
    Unzips all .zip files in the specified directory.

    Args:
        directory (str): The path to the directory to scan for .zip files.
    """
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # List all files in the directory
    files = os.listdir(directory)

    # Process each file in the directory
    for file in files:
        if file.endswith('.zip'):
            zip_path = os.path.join(directory, file)
            extract_dir = os.path.join(directory, os.path.splitext(file)[0])

            # Create a folder for the unzipped contents
            os.makedirs(extract_dir, exist_ok=True)

            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_dir)
                print(f"Unzipped '{file}' into '{extract_dir}'.")
            except zipfile.BadZipFile:
                print(f"Error: '{file}' is not a valid zip file.")

if __name__ == "__main__":
    # Specify the directory to check
    directory_to_check = input("Enter the path to the directory: ").strip()
    unzip_files_in_directory(directory_to_check)

