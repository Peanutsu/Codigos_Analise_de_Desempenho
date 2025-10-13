import time
import platform
import psutil
import sys
import os
import tracemalloc

def bubble_sort(arr):
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
    return numbers

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def main():
    # System information
    print(f"Linguagem: Python {sys.version}")
    print(f"Sistema: {platform.system()} {platform.release()}")
    print(f"Processador: {platform.processor()}")
    print(f"Memoria total: {psutil.virtual_memory().total // (1024**3)} GB")
    print(f"Algoritmo: Bubble Sort")
    print("-" * 50)

    # Create resultados folder if it doesn't exist
    resultados_folder = "resultados"
    if not os.path.exists(resultados_folder):
        os.makedirs(resultados_folder)

    # Read input file
    input_file = "input.txt"
    output_file = os.path.join(resultados_folder, "arq-saida-python-bubble.txt")

    numbers = read_numbers_from_file(input_file)

    # Start tracing memory allocations
    tracemalloc.start()

    # Measure execution time
    start_time = time.time()
    sorted_numbers = bubble_sort(numbers.copy())
    end_time = time.time()

    # Get memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memory_used = peak / 1024  # Convert to KB

    # Write output file
    write_numbers_to_file(output_file, sorted_numbers)

    # Print results
    execution_time_ms = (end_time - start_time) * 1000
    print(f"Tempo de execução: {execution_time_ms:.2f} ms")
    print(f"Memoria utilizada: {memory_used:.2f} KB")
    print(f"Arquivo de saída: {output_file}")

if __name__ == "__main__":
    main()