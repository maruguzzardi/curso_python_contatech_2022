awarded = []
for i in range(6):
    awarded.append(int(input("Ingresá un número ganador: ")))
awarded.sort()
print(f"Los números ganadores son {awarded}")
