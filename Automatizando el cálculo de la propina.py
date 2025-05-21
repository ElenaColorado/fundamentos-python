total_de_la_cuenta = float(input("Ingresa el total de la cuenta: $"))
porcentaje_propina = float(input("Ingresa el porcentaje de propina: %"))

propina = total_de_la_cuenta * (porcentaje_propina / 100)
total_con_propina = total_de_la_cuenta + propina

print(f"Total de la cuenta: ${total_de_la_cuenta:.2f}")
print(f"Propina: ${propina:.2f}")
print(f"Total de la cuenta con propina: ${total_con_propina:.2f}")
