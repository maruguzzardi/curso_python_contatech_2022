CLOWN_WEIGHT = 112
WRIST_WEIGHT = 75
clowns = int(input("Ingresá el número de payasos a enviar: "))
wrists = int(input("Ingresá el número de muñecas a enviar: "))
total_weight_clowns = CLOWN_WEIGHT * clowns
total_weight_wrists = WRIST_WEIGHT * wrists
total_weight = total_weight_clowns + total_weight_wrists
print(f"El peso total del paquete es {total_weight}")
