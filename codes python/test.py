
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import os
m=0
def cpu_heavy_computation(x):
    global m
    while True:
        global m
        result = 0
        m=1
        for i in range(1, 10**7):  # Heavy loop
            result += np.sin(i) ** 2 + np.cos(i) ** 2
            if m==1:
                return 0
        
        

def main():
    global m
    cpu_cores = os.cpu_count()  # Get number of CPU cores
    print(f"Number of CPU cores: {cpu_cores}")
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        # Submit tasks for each core
        futures = [executor.submit(cpu_heavy_computation, 100) for _ in range(cpu_cores)]
        
        # Wait for all processes to complete and get their results
        results = [future.result() for future in futures]
        
    # Print all the results
    print("Results from all processes:")
    for result in results:
        print(result)
    print(m)

if __name__ == '__main__':
    main()
