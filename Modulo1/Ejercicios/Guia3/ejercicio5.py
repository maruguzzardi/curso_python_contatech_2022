age = int(input("¿Cuál es tu edad? "))
income = float(input("¿Cuales son tus ingresos mensuales?"))
if age <= 16 or income < 1000:
    print("No tienes que cotizar")
else:
    print("Tienes que cotizar")
