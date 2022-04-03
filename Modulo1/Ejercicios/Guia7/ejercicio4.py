def invoice(amount: float, vat: int = 21) -> float:
    return amount + amount * vat / 100


print(invoice(1000, 10))
print(invoice(1000))
