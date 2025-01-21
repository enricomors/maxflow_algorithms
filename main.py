import subprocess
from codecarbon import OfflineEmissionsTracker
import argparse
import os
import pandas as pd


def run_cpp_program(executable, dataset, algorithm):
    # Define the output file for CodeCarbon
    emissions_file = "emissions.csv"

    # Initialize the CodeCarbon emission tracker
    tracker = OfflineEmissionsTracker(country_iso_code="ITA", output_file=emissions_file)
    tracker.start()

    try:
        # Define the command and its arguments as a list
        command = [executable, dataset, algorithm]

        # Call the C++ program using subprocess
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Print the output and errors from the C++ program
        print("Output from C++ program:")
        print(result.stdout)

        if result.stderr:
            print("Errors from C++ program:")
            print(result.stderr)

        # Check if the program exited with an error
        if result.returncode != 0:
            print(f"Program exited with return code: {result.returncode}")

    except Exception as e:
        print(f"An error occurred while running the C++ program: {e}")

    finally:
        # Stop the tracker and print the emission report
        emissions = tracker.stop()
        print(f"Emissions: {emissions} kg CO2e")

        # Inspect the emissions.csv file for additional metrics
        if os.path.exists(emissions_file):
            try:
                # Load the CSV file
                df = pd.read_csv(emissions_file)

                # Get the last row (latest execution)
                latest_metrics = df.iloc[-1]

                # Extract and print desired metrics
                print("\nAdditional Metrics:")
                print(f"CO2eRate (kg/s): {latest_metrics['emissions_rate']}")
                print(f"CPU Energy (kWh): {latest_metrics['cpu_energy']}")
                print(f"RAM Energy (kWh): {latest_metrics['ram_energy']}")
                print(f"Total Energy (kWh): {latest_metrics['energy_consumed']}")
                print(f"Country: {latest_metrics['country_name']}")
                print(f"CPU Count: {latest_metrics['cpu_count']}")
            except Exception as e:
                print(f"Error reading emissions file: {e}")
        else:
            print(f"Emissions file '{emissions_file}' not found.")


if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Run a C++ program with CodeCarbon emission tracking.")
    parser.add_argument("-e", "--executable", type=str, help="Path to the C++ executable.")
    parser.add_argument("-d", "--dataset", type=str, help="Path to the Dataset")
    parser.add_argument("-a", "--algorithm", type=str, help="Algorithm to benchmark")

    # Parse the arguments
    args = parser.parse_args()

    # Run the C++ program with the provided arguments
    run_cpp_program(args.executable, args.dataset, args.algorithm)
