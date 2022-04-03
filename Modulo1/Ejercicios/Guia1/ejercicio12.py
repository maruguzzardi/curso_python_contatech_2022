bread = int(input("Ingresá el número de barras vendidas que no son frescas: "))
PRICE = 3.49
DISCOUNT = 0.6
final_price = bread * PRICE * (1 - DISCOUNT)
print(f"El coste de una barra fresca es ${PRICE}")
print(f"El descuento sobre una barra no fresca es {DISCOUNT * 100}%")
print(f"El coste final a pagar es ${round(final_price, 2)}")
