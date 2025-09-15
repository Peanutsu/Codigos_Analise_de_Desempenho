import sys
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
    
    def adicionar(self, valor, posicao):
        novo_no = No(valor)
        
        if posicao == 0:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
            return
        
        atual = self.cabeca
        for i in range(posicao - 1):
            if atual is None:
                return
            atual = atual.proximo
        
        if atual is None:
            return
        
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
    
    def remover(self, valor):
        if self.cabeca == None:
            raise ValueError("{} is not in list".format(valor))
        elif self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            return True
        else:
            ancestor = self.cabeca
            pointer = self.cabeca.proximo
            while(pointer):
                if pointer.valor == valor:
                    ancestor.proximo = pointer.proximo
                    pointer.proximo = None
                    return True
                ancestor = pointer
                pointer = pointer.proximo
        raise ValueError("{} is not in list".format(valor))


    
    def imprimir(self):
        valores = []
        atual = self.cabeca
        while atual:
            valores.append(atual.valor)
            atual = atual.proximo
        print(valores)

def processar_arquivo(nome_arquivo):
    lista = ListaEncadeada()
    
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    

    valores_iniciais = list(map(int, linhas[0].strip().split()))
    for valor in valores_iniciais:
        lista.adicionar(valor, 0)
    

    quantidade_acoes = int(linhas[1].strip())
    

    for i in range(2, 2 + quantidade_acoes):
        linha = linhas[i].strip().split()
        acao = linha[0]
        
        if acao == 'A':
            valor = int(linha[1])
            posicao = int(linha[2])
            lista.adicionar(valor, posicao)
        elif acao == 'R':
            deletado = int(linha[1])
            lista.remover(deletado)
        elif acao == 'P':
            lista.imprimir()
if __name__ == "__main__":
    if len(sys.argv)>1:
        arquivo = sys.argv[1]
        processar_arquivo(arquivo) #parametros da main ou args