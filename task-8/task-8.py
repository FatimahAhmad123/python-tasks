#!/usr/bin/python3
import argparse
import numpy as np

def calculate_statistics(file_path):
    try:
        # Read data from the text file
        data = np.loadtxt(file_path)

        # Calculate statistics
        mean = np.mean(data)
        median = np.median(data)
        max_value = np.max(data)
        min_value = np.min(data)
        std_dev = np.std(data)
        percentiles = np.percentile(data, [99, 99.9, 99.99, 99.999])

        # Print the calculated statistics
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Max: {max_value}")
        print(f"Min: {min_value}")
        print(f"Standard Deviation: {std_dev}")
        print(f"99th Percentile: {percentiles[0]}")
        print(f"99.9th Percentile: {percentiles[1]}")
        print(f"99.99th Percentile: {percentiles[2]}")
        print(f"99.999th Percentile: {percentiles[3]}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate statistics from a text file.")
    parser.add_argument("file_path", type=str, help="Path to the text file")
    args = parser.parse_args()

    calculate_statistics(args.file_path)
