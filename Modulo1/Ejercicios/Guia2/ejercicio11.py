product = input('Ingresá el nombre del producto: ')
price = float(input('Ingresá el precio unitario: '))
count = int(input('Ingresá el número de unidades: '))
total = count * price
print(f'{product}: {count:3d} unidades x ${price:9.2f} = ${total:11.2f}')
