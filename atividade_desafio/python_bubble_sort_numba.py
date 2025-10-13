import time
import platform
import psutil
import sys
import os
import tracemalloc
import numpy as np
from numba import jit

@jit(nopython=True)
def bubble_sort_numba(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
    return np.array(numbers, dtype=np.int32)

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def main():

    print(f"Linguagem: Python {sys.version}")
    print(f"Sistema: {platform.system()} {platform.release()}")
    print(f"Processador: {platform.processor()}")
    print(f"Memoria total: {psutil.virtual_memory().total // (1024**3)} GB")
    print(f"Algoritmo: Bubble Sort (Numba JIT)")
    print("-" * 50)


    resultados_folder = "resultados"
    if not os.path.exists(resultados_folder):
        os.makedirs(resultados_folder)


    input_file = "input.txt"
    output_file = os.path.join(resultados_folder, "arq-saida-python-bubble-numba.txt")

    numbers = read_numbers_from_file(input_file)


    print("Aquecendo JIT compiler...")
    test_array = np.array([3, 1, 4, 1, 5], dtype=np.int32)
    bubble_sort_numba(test_array.copy())
    print("JIT compilado!")


    tracemalloc.start()


    start_time = time.time()
    sorted_numbers = bubble_sort_numba(numbers.copy())
    end_time = time.time()


    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memory_used = peak / 1024 


    write_numbers_to_file(output_file, sorted_numbers)


    execution_time_ms = (end_time - start_time) * 1000
    print(f"Tempo de execução: {execution_time_ms:.2f} ms")
    print(f"Memoria utilizada: {memory_used:.2f} KB")
    print(f"Arquivo de saída: {output_file}")

if __name__ == "__main__":
    main()