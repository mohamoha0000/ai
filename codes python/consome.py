import multiprocessing
import numpy as np
from numba import cuda, jit
import time

# 🚀 CPU-intensive function
#@jit(nopython=True)
def cpu_heavy_computation(x):
    result = 0
    for i in range(1, 10**7):  # Heavy loop
        result += np.sin(i) ** 2 + np.cos(i) ** 2
    return result


def cpu_worker():
    while True:
        cpu_heavy_computation(100)


if __name__ == '__main__':
    cpu_cores = multiprocessing.cpu_count()
    print(f"Number of CPU cores: {cpu_cores}")
    cpu_processes = [multiprocessing.Process(target=cpu_worker) for _ in range(cpu_cores)]

    for p in cpu_processes:
        p.start()
