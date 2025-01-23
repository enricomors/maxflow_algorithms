import argparse
import os


def list_files_with_paths_to_txt(directory, output_file):
    try:
        # Get the list of all files in the directory
        files = os.listdir(directory)

        # Filter out directories, keep only files
        file_paths = [os.path.join(directory, f) for f in files if os.path.isfile(os.path.join(directory, f))]

        # Write the file paths to the output text file
        with open(output_file, 'w') as f:
            for file_path in file_paths:
                f.write(file_path + '\n')

        print(f"File paths have been successfully written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="directory in which to read files")
    parser.add_argument("outfile", help="filepath in which to write file names")
    args = parser.parse_args()
    # Specify the directory and the output file name
    directory_path = args.directory
    output_txt = args.outfile

    list_files_with_paths_to_txt(directory_path, output_txt)
