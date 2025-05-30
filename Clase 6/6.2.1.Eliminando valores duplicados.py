'''
Clase:        #6
Tema:         Listas y bucles
Ejercicio:    6.2.1. Eliminando valores duplicados
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2

Autor:        Elena Fabiola Colorado Mejía
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

lista=input("Ingresa  una lista de números:")
lista=list(lista.split())
resultado=[]
for número in lista:
    if número not in resultado:
        resultado.append(número)
    else:
        continue
print(" ".join(resultado))