lista = input("Ingresa una lista de números: ")
lista = lista.split()  
lideres = []
max_derecha = float('-inf')


for i in range(len(lista) - 1, -1, -1):
    numero = int(lista[i])  
    if numero > max_derecha:
        lideres.append(str(numero)) 
        max_derecha = numero

lideres.reverse()

print(" ".join(lideres))

