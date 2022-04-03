def to_decimal(number: str) -> float:
    number = list(number)
    number.reverse()
    decimal = 0
    for i in range(len(number)):
        decimal += int(number[i]) * 2 ** i
    return decimal


def to_binary(number: float) -> str:
    binary = []
    while number > 0:
        binary.append(str(number % 2))
        number //= 2
    binary.reverse()
    return ''.join(binary)


print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))
