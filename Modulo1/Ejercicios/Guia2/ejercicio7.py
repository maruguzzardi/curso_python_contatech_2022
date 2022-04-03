email = input("Ingresá tu correo electrónico: ")
formatted_email = email[:email.find('@')] + '@ceu.es'
print(formatted_email)
