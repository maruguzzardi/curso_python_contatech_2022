date = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
day = date[:date.find('/')]
year_moth = date[date.find('/') + 1:]
month = year_moth[:year_moth.find('/')]
year = year_moth[year_moth.find('/') + 1:]
print('Día', day)
print('Mes', month)
print('Año', year)

