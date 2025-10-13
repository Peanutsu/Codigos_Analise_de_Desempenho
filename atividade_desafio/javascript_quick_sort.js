const fs = require('fs');
const os = require('os');

function quickSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }

    const pivot = arr[Math.floor(arr.length / 2)];
    const left = arr.filter(x => x < pivot);
    const middle = arr.filter(x => x === pivot);
    const right = arr.filter(x => x > pivot);

    return [...quickSort(left), ...middle, ...quickSort(right)];
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
    console.log(`Algoritmo: Quick Sort`);
    console.log("-".repeat(50));

    // Create resultados folder if it doesn't exist
    const resultadosFolder = "resultados";
    if (!fs.existsSync(resultadosFolder)) {
        fs.mkdirSync(resultadosFolder);
    }

    // Read input file
    const inputFile = "input.txt";
    const outputFile = `${resultadosFolder}/arq-saida-javascript-quick.txt`;

    const numbers = readNumbersFromFile(inputFile);

    // Measure memory before sorting
    const memoryBefore = getMemoryUsage();

    // Measure execution time
    const startTime = process.hrtime.bigint();
    const sortedNumbers = quickSort([...numbers]);
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