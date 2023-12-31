#!/usr/bin/python3
import argparse
import numpy as np

def calculate_statistics(file_path):

        # Reading data from the text file
    data = np.loadtxt(file_path) # load data from a text file, provided that each row in the file has the same number of features or values 

    # Print the calculated statistics
    print("Mean:",np.mean(data))
    print("Median:",np.median(data))
    print("Max:",np.max(data))
    print("Min:",np.min(data))
    print("Standard Deviation:",np.std(data))
    print("99th Percentile:",np.percentile(data, 99))
    print("99.9th Percentile:",np.percentile(data, 99.9))
    print("99.99th Percentile:",np.percentile(data, 99.99))
    print("99.999th Percentile:",np.percentile(data, 99.999))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the text file")
    args = parser.parse_args()

    calculate_statistics(args.file_path)
