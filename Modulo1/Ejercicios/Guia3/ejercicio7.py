income = float(input("¿Cuál es tu renta anual? "))
if income < 10000:
    tipo = 5
elif income < 20000:
    tipo = 15
elif income < 35000:
    tipo = 20
elif income < 60000:
    tipo = 30
else:
    tipo = 45
tax = income * tipo / 100
print("Tienes que pagar $", tax)
