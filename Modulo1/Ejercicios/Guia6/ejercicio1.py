coins = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
coin = input("Ingresá una divisa: ")
print(coins.get(coin.title(), "La divisa no está."))
