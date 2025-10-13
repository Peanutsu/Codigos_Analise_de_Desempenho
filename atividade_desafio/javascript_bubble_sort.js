const fs = require('fs');
const os = require('os');

function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    return arr;
}

function readNumbersFromFile(filename) {
    const data = fs.readFileSync(filename, 'utf8');
    return data.trim().split('\n').map(line => parseInt(line.trim()));
}

function writeNumbersToFile(filename, numbers) {
    const content = numbers.join('\n') + '\n';
    fs.writeFileSync(filename, content);
}

function getMemoryUsage() {
    return process.memoryUsage().rss / 1024; // Convert to KB
}

function main() {
    // System information
    console.log(`Linguagem: Node.js ${process.version}`);
    console.log(`Sistema: ${os.type()} ${os.release()}`);
    console.log(`Processador: ${os.cpus()[0].model}`);
    console.log(`Memoria total: ${Math.round(os.totalmem() / (1024**3))} GB`);
    console.log(`Algoritmo: Bubble Sort`);
    console.log("-".repeat(50));

    // Create resultados folder if it doesn't exist
    const resultadosFolder = "resultados";
    if (!fs.existsSync(resultadosFolder)) {
        fs.mkdirSync(resultadosFolder);
    }

    // Read input file
    const inputFile = "input.txt";
    const outputFile = `${resultadosFolder}/arq-saida-javascript-bubble.txt`;

    const numbers = readNumbersFromFile(inputFile);

    // Measure memory before sorting
    const memoryBefore = getMemoryUsage();

    // Measure execution time
    const startTime = process.hrtime.bigint();
    const sortedNumbers = bubbleSort([...numbers]);
    const endTime = process.hrtime.bigint();

    // Measure memory after sorting
    const memoryAfter = getMemoryUsage();
    const memoryUsed = memoryAfter - memoryBefore;

    // Write output file
    writeNumbersToFile(outputFile, sortedNumbers);

    // Print results
    const executionTimeMs = Number(endTime - startTime) / 1000000; // Convert nanoseconds to milliseconds
    console.log(`Tempo de execução: ${executionTimeMs.toFixed(2)} ms`);
    console.log(`Memoria utilizada: ${memoryUsed.toFixed(2)} KB`);
    console.log(`Arquivo de saída: ${outputFile}`);
}

main();