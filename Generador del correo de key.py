nombre=input("Ingresa tu nombre completo:")
partes = nombre.strip().split()
primer_nombre = partes[0].lower()
primer_apellido = partes[2].lower()
correo = f"{primer_nombre}.{primer_apellido}@keyinstitute.edu.sv"
print(f"El correo que se debe asignar al usuario ingresado es: {correo}")
