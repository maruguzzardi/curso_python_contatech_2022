a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for index in range(len(a)):
    product += a[index] * b[index]
print(f"El producto de los vectores {a} y {b} es {product}")
