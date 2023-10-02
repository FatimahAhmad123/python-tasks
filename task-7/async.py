#!/usr/bin/python3
import asyncio
import logging
import time

# Configure the logging
logging.basicConfig(filename="async.log", level=logging.INFO)

async def find_divisibles(inrange, div_by):
    logging.info("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    
    start_time = time.time()  
    
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 5000 == 0:
            await asyncio.sleep(0.0)
            
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time

    logging.info("Done w/ nums in range {} divisible by {} (Time taken: {:.4f} seconds)".format(inrange, div_by, elapsed_time))
    return located

async def main():
    divs1 = loop.create_task(find_divisibles(50800000, 34113))
    divs2 = loop.create_task(find_divisibles(100052,3210))
    divs3 = loop.create_task(find_divisibles(20000,5))
    await asyncio.gather(divs1,divs2,divs3)
    return divs1, divs2, divs3


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(0)
        d1, d2, d3 = loop.run_until_complete(main())
        
    except Exception as e:
        
          logging.error(f"An error occurred: {str(e)}")

    finally:
        loop.close()