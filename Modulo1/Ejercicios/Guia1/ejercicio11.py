INTEREST = 0.04
investment = float(input("Ingresá la inversión inicial: "))
balance = investment * (1 + INTEREST)
print("Balance tras el primer año:" + str(round(balance, 2)))
balance = balance * (1 + INTEREST)
print("Balance tras el segundo año:" + str(round(balance, 2)))
balance = balance * (1 + INTEREST)
print("Balance tras el tercer año:" + str(round(balance, 2)))
