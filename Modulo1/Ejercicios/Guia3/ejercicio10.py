print("Bienvenido a la pizzeria Bella Napoli.")
print("Tipos de pizza")
print("\t1- Vegetariana\n\t2- No vegetariana\n")
number_type = input("Introduce el número correspondiente al tipo de pizza que quieres:")
if number_type == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingredient = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingredient == "1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingredient = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ")
    if ingredient == "1":
        print("peperoni")
    elif ingredient == "2":
        print("jamón")
    else:
        print("salmón")
