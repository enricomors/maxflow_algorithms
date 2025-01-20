import subprocess
from codecarbon import OfflineEmissionsTracker
import argparse

def run_cpp_program(executable, dataset, algorithm):
    # Initialize the CodeCarbon emission tracker
    tracker = OfflineEmissionsTracker(country_iso_code="ITA")
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
