import time
import platform
import psutil
import sys
import os
import tracemalloc

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def main():
    
    print(f"Linguagem: Python {sys.version}")
    print(f"Sistema: {platform.system()} {platform.release()}")
    print(f"Processador: {platform.processor()}")
    print(f"Memoria total: {psutil.virtual_memory().total // (1024**3)} GB")
    print(f"Algoritmo: Quick Sort")
    print("-" * 50)

    
    resultados_folder = "resultados"
    if not os.path.exists(resultados_folder):
        os.makedirs(resultados_folder)

    
    input_file = "input.txt"
    output_file = os.path.join(resultados_folder, "arq-saida-python-quick.txt")

    numbers = read_numbers_from_file(input_file)

    
    tracemalloc.start()

    
    start_time = time.time()
    sorted_numbers = quicksort(numbers.copy())
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