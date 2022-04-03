PASSWORD = "contraseña"
user_input = input("Ingresá la contraseña: ")
if PASSWORD == user_input.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")
