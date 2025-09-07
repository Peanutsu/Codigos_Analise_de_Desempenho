#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void crivo_era(int n, bool *eh_primo, int *primos, int *quantidade) {
    
    for (int i = 0; i <= n; i++) {
        eh_primo[i] = true;
    }
    eh_primo[0] = eh_primo[1] = false;
    
    for (int i = 2; i * i <= n; i++) {
        if (eh_primo[i]) {
            for (int j = i * i; j <= n; j += i) {
                eh_primo[j] = false;
            }
        }
    }
    *quantidade = 0;
    for (int i = 2; i <= n; i++) {
        if (eh_primo[i]) {
            primos[*quantidade] = i;
            (*quantidade)++;
        }
    }
}

int validar_entrada(char *entrada) {
    for (int i = 0; i < strlen(entrada); i++) {
        if (entrada[i] < '0' || entrada[i] > '9') {
            return -1;
        }
    }
    
    int numero = atoi(entrada);
    if (numero < 1) {
        return -1;
    }
    
    return numero;
}

void exibir_resultados(int n, int *primos, int quantidade) {
    printf("\n=== RESULTADOS ===\n");
    printf("Valor de N: %d\n", n);
    printf("Quantidade de números primos encontrados: %d\n", quantidade);
    
    if (quantidade > 0) {
        printf("Números primos no intervalo de 1 a %d:\n", n);
        for (int i = 0; i < quantidade; i++) {
            printf("%4d", primos[i]);
            if ((i + 1) % 10 == 0) {
                printf("\n");
            }
        }
        if (quantidade % 10 != 0) {
            printf("\n");
        }
    } else {
        printf("Nenhum número primo encontrado no intervalo de 1 a %d.\n", n);
    }
    printf("==================\n");
}
int main() {
    char entrada[100];
    int n;
    printf("=== CONTADOR DE NÚMEROS PRIMOS ===\n");
    printf("Este programa encontra todos os números primos de 1 até N.\n");
    printf("Utilizando o algoritmo Crivo de Eratóstenes para busca eficiente.\n\n");
    
    while (1) {
        printf("Digite um número inteiro N > 0 (ou 'sair' para encerrar): ");
        
        if (scanf("%s", entrada) != 1) {
            printf("Erro na leitura da entrada.\n");
            continue;
        }
        
        if (strcmp(entrada, "sair") == 0 || strcmp(entrada, "SAIR") == 0) {
            printf("Programa encerrado.\n");
            break;
        }
        
        n = validar_entrada(entrada);
        if (n == -1) {
            printf("ERRO: Digite apenas números inteiros maiores que 0.\n");
            printf("Exemplo de entrada válida: 50\n\n");
            continue;
        }
        
        printf("\nProcessando... Buscando primos até %d\n", n);
        
        bool *eh_primo = (bool*)malloc((n + 1) * sizeof(bool));
        int *primos = (int*)malloc(n * sizeof(int)); // No máximo n primos
        int quantidade;
        
        if (eh_primo == NULL || primos == NULL) {
            printf("Erro: Não foi possível alocar memória.\n");
            if (eh_primo) free(eh_primo);
            if (primos) free(primos);
            continue;
        }
        
        crivo_era(n, eh_primo, primos, &quantidade);
        
        exibir_resultados(n, primos, quantidade);

        free(eh_primo);
        free(primos);
        
        printf("\n");
    }
    
    return 0;
}