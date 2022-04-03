price = input("Ingresá el precio del producto con dos decimales:  ")
print(price[:price.find('.')], 'pesos y', price[price.find('.') + 1:], 'centavos.')
