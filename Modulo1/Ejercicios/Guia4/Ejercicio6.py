# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
# rectángulo como el de más abajo, de altura el número introducido.

height = int(input("Ingresá la altura del triángulo: "))
triangulo = ""
for index in range(0, height):
    triangulo = triangulo + "*"
    print(triangulo)
print("FIN")
