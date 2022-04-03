award = 2400
INSUFFICIENT = 0
ACCEPTABLE = 0.4
MERITORIOUS = 0.6
score = float(input("Introduce tu puntuación: "))
if score == INSUFFICIENT:
    level = "Inaceptable"
elif score == ACCEPTABLE:
    level = "Aceptable"
elif score >= 0.6:
    level = "Meritorio"
else:
    level = ""
if level == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % level)
    print("Te corresponde cobrar $ %.2f" % (score * award))
