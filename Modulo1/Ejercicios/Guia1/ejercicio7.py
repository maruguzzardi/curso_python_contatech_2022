user_height = input("Ingresá tu altura: ")
user_weight = input("Ingresá tu peso: ")
body_mass_number = round(float(user_weight) / float(user_height) ** 2.2)
print(f'Tu índice de masa corporal es {body_mass_number}')
