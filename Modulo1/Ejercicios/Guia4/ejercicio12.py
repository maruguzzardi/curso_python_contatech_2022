words = input("Ingresá una frase: ")
letter = input("Ingresá una letra: ")
contador = 0
for index in words:
    if index == letter:
        contador += 1
print(f"La letra {letter} aparece %2i veces en la frase {words}." % contador)
