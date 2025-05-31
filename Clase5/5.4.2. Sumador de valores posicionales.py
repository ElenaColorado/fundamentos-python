'''
Clase:        #5
Tema:         Listas y bucles
Ejercicio:    5.4.2 Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2

Autor:        Elena Fabiola Colorado Mejía
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''
numero = int(input("Ingresa un número: "))

print(f"Proceso de reducción para {numero}:")

while numero >= 10:
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    print(f"{numero} = {suma}")
    numero = suma

print(f"El resultado final es: {numero}")
