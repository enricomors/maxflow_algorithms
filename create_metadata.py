import argparse
import os


def process_dimacs_directory(input_directory, output_file):
    """
    Processes a directory of DIMACS files and writes the number of nodes and arcs for each file to an output file.

    Args:
        input_directory (str): Path to the directory containing DIMACS files.
        output_file (str): Path to the output file to write results.
    """
    results = []

    # Iterate through all files in the directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".max"):  # Adjust file extension if necessary
            file_path = os.path.join(input_directory, filename)
            num_nodes, num_arcs = parse_dimacs_file(file_path)

            if num_nodes is not None and num_arcs is not None:
                results.append(f"{filename}.bbk -> ({num_nodes}, {num_arcs})")
            else:
                print(f"Warning: Could not process file {filename}.")

    # Write results to the output file
    with open(output_file, "w") as f_out:
        f_out.write("\n".join(results))
    print(f"Results written to {output_file}")


def parse_dimacs_file(file_path):
    """
    Parse a DIMACS max-flow file and extract the number of nodes and arcs.

    Args:
        file_path (str): Path to the DIMACS file.

    Returns:
        tuple: (num_nodes, num_arcs) or (None, None) if parsing fails.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Skip comment lines
                if line.startswith("c"):
                    continue

                # Process the problem line
                if line.startswith("p"):
                    parts = line.strip().split()
                    if len(parts) >= 4 and parts[1] == "max":
                        num_nodes = int(parts[2])
                        num_arcs = int(parts[3])
                        return num_nodes, num_arcs
        return None, None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None, None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_directory", help="path of the .csv file to update")
    args = parser.parse_args()

    output_file = "metadata.txt"
    process_dimacs_directory(args.input_directory, output_file)
