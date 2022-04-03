sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for index in range(n):
    sample[index] = int(sample[index])
sample = tuple(sample)
add = 0
sumsq = 0
for index in sample:
    add += index
    sumsq += index ** 2
mean = add / n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)
