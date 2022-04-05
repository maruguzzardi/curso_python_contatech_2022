MIN_HEIGHT = 1.5
MIN_AGE = 18
user_age = input("Ingresá tu edad: \n")
user_height = input("Ingresá tu altura: \n")
is_age_valid = int(user_age) >= MIN_AGE
is_height_valid = float(user_height) >= MIN_HEIGHT

if is_age_valid and is_height_valid:
    print("Puede ingresar al juego.")
elif not is_age_valid:
    print("No puede ingresar al juego por la edad.")
elif not is_height_valid:
    print("No puede ingresar al juego por la altura.")
