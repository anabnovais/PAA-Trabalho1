import time
import random
def shellSort (lista):
        intervalo = 1 
        tamanho_lista = len(lista)
        while (intervalo < tamanho_lista):
            intervalo = 3 * intervalo + 1
        while (intervalo > 1):
            intervalo //= 3
            for indice_atual in range(intervalo, tamanho_lista):
                valor_atual = lista[indice_atual]
                indice_anterior = indice_atual
                while (indice_anterior >= intervalo and lista[indice_anterior - intervalo] > valor_atual):
                    lista[indice_anterior] = lista[indice_anterior - intervalo]
                    indice_anterior -= intervalo
                lista[indice_anterior] = valor_atual

def testarShellSort(tamanho_lista):
    crescente = list(range(tamanho_lista))
    inicio = time.time()
    shellSort(crescente)
    fim = time.time()
    print(f"Crescente: {fim - inicio:.5f} segundos")

    decrescente = list(range(tamanho_lista, 0, -1))
    inicio = time.time()
    shellSort(decrescente)
    fim = time.time()
    print(f"Decrescente: {fim - inicio:.5f} segundos")

    aleatorio = random.sample(range(tamanho_lista * 2), tamanho_lista)
    inicio = time.time()
    shellSort(aleatorio)
    fim = time.time()
    print(f"Aleatório: {fim - inicio:.5f} segundos\n")



if __name__ == "__main__":
    print("Testando Shell Sort com 20.000 elementos:\n")
    testarShellSort(20000)
    print("Testando Shell Sort com 40.000 elementos:\n")
    testarShellSort(40000)
    print("Testando Shell Sort com 60.000 elementos:\n")
    testarShellSort(60000)