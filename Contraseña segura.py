contraseña = input("Ingresa tu contraseña: ")
longitud = len(contraseña)
numero = 0
mayuscula = 0

for letra in contraseña:
    if letra.isdigit():
        numero = 1
    if letra.isupper():
        mayuscula = 1

if longitud >= 8 and numero == 1 and mayuscula == 1:
    print("Contraseña segura")
else:
    print("Contraseña no segura")

