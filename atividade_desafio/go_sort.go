package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime"
	"strconv"
	"strings"
	"time"
)

func bubbleSort(arr []int) []int {
	n := len(arr)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	return arr
}

func quickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	pivot := arr[len(arr)/2]
	var left, middle, right []int

	for _, x := range arr {
		if x < pivot {
			left = append(left, x)
		} else if x == pivot {
			middle = append(middle, x)
		} else {
			right = append(right, x)
		}
	}

	result := make([]int, 0, len(arr))
	result = append(result, quickSort(left)...)
	result = append(result, middle...)
	result = append(result, quickSort(right)...)

	return result
}

func readNumbersFromFile(filename string) ([]int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var numbers []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			num, err := strconv.Atoi(line)
			if err != nil {
				return nil, err
			}
			numbers = append(numbers, num)
		}
	}
	return numbers, scanner.Err()
}

func writeNumbersToFile(filename string, numbers []int) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	for _, num := range numbers {
		fmt.Fprintf(writer, "%d\n", num)
	}
	return writer.Flush()
}

func getMemoryUsage() uint64 {
	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	return m.Alloc
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Uso: go run go_sort.go [bubble|quick]")
		fmt.Println("Exemplo: go run go_sort.go bubble")
		return
	}

	algorithm := strings.ToLower(os.Args[1])
	if algorithm != "bubble" && algorithm != "quick" {
		fmt.Println("Algoritmo inválido! Use 'bubble' ou 'quick'")
		return
	}

	var algorithmName string
	var outputFile string
	var sortFunc func([]int) []int

	if algorithm == "bubble" {
		algorithmName = "Bubble Sort"
		outputFile = "resultados/arq-saida-go-bubble.txt"
		sortFunc = bubbleSort
	} else {
		algorithmName = "Quick Sort"
		outputFile = "resultados/arq-saida-go-quick.txt"
		sortFunc = quickSort
	}

	fmt.Printf("Linguagem: Go %s\n", runtime.Version())
	fmt.Printf("Sistema: %s\n", runtime.GOOS)
	fmt.Printf("Arquitetura: %s\n", runtime.GOARCH)
	fmt.Printf("Algoritmo: %s\n", algorithmName)
	fmt.Println(strings.Repeat("-", 50))

	resultadosFolder := "resultados"
	if _, err := os.Stat(resultadosFolder); os.IsNotExist(err) {
		os.Mkdir(resultadosFolder, 0755)
	}

	inputFile := "input.txt"

	numbers, err := readNumbersFromFile(inputFile)
	if err != nil {
		fmt.Printf("Erro ao ler arquivo: %v\n", err)
		return
	}

	runtime.GC()
	runtime.GC()

	memoryBefore := getMemoryUsage()
	startTime := time.Now()

	numbersCopy := make([]int, len(numbers))
	copy(numbersCopy, numbers)
	sortedNumbers := sortFunc(numbersCopy)

	endTime := time.Now()

	memoryAfter := getMemoryUsage()
	memoryUsed := float64(memoryAfter-memoryBefore) / 1024

	err = writeNumbersToFile(outputFile, sortedNumbers)
	if err != nil {
		fmt.Printf("Erro ao escrever arquivo: %v\n", err)
		return
	}

	executionTimeMs := float64(endTime.Sub(startTime).Nanoseconds()) / 1000000
	fmt.Printf("Tempo de execução: %.2f ms\n", executionTimeMs)
	fmt.Printf("Memoria utilizada: %.2f KB\n", memoryUsed)
	fmt.Printf("Arquivo de saída: %s\n", outputFile)
}