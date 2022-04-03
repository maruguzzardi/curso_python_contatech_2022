age = int(input("Ingresá tu edad: "))
BABY_AGE = 4
BABY_PRICE = 0
YOUNG_AGE = 18
YOUNG_PRICE = 4
ADULT_PRICE = 10
if age < BABY_AGE:
    price = BABY_PRICE
elif age <= YOUNG_AGE:
    price = YOUNG_PRICE
else:
    price = ADULT_PRICE
print("El precio de la entrada es $", price)
