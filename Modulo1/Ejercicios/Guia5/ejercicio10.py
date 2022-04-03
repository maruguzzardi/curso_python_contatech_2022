prices = [50, 75, 46, 22, 80, 65, 8]
minimum = maximum = prices[0]
for price in prices:
    if price < minimum:
        minimum = price
    elif price > maximum:
        maximum = price
print(f"El mínimo es {minimum}")
print(f"El máximo es {maximum}")
