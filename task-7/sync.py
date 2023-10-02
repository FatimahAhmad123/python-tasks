#!/usr/bin/python3
import logging
import time

# Configure the logging
logging.basicConfig(filename="sync.log", level=logging.INFO)

def find_divisibles(inrange, div_by):
    logging.info("Finding numbers in range {} divisible by {}".format(inrange, div_by))
    located = [] 
    start_time = time.time()  # Record the start time

    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
            
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    
    logging.info("Done with numbers in range {} divisible by {} (Time taken: {:.4f} seconds)".format(inrange, div_by, elapsed_time))
    return located

def main():
    divs1 = find_divisibles(50800000, 34113)
    divs2 = find_divisibles(100052,3210)
    divs3 = find_divisibles(20000,5)
    return divs1, divs2, divs3

if __name__ == "__main__":
    try:
        d1, d2, d3 = main()
        # print(d1)
        # print(d2)
        # print(d3)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        pass
