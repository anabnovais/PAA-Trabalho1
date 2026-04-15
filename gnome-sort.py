import random

def gerar_vetor_aleatorio(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]

def gerar_vetor_ordenado(tamanho):
    return list(range(1, tamanho + 1))

def gerar_vetor_invertido(tamanho):
    return list(range(tamanho, 0, -1))

# vetor = [5, 2, 9, 1, 5, 6]
vetor = gerar_vetor_aleatorio(10)

def troca(vetor, i):
    aux = vetor[i]
    vetor[i] = vetor[i-1]
    vetor[i-1] = aux

def gnome_sort(vetor):
    tamanho = len(vetor)
    i = 1
    while i < tamanho:
        if i == 0 or vetor[i] >= vetor[i-1]:
            i = i + 1
        else:
            troca(vetor, i)
            i = i - 1
            
print("Vetor original: ")
for i in range(len(vetor)):
    print(vetor[i], end=' ')
print("\n")

gnome_sort(vetor)

print("Vetor ordenado: ")
for i in range(len(vetor)):
    print(vetor[i], end=' ')