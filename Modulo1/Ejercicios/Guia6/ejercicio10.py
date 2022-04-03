clients = {}
option = ''
while option != '6':
    if option == '1':
        client_id = input('Introduce ID del cliente: ')
        name = input('Introduce el nombre del cliente: ')
        address = input('Introduce la dirección del cliente: ')
        phone = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        client = {'nombre': name, 'dirección': address, 'teléfono': phone, 'email': email, 'preferente': vip == 'S'}
        clients[client_id] = client
    if option == '2':
        client_id = input('Introduce ID del cliente: ')
        if client_id in clients:
            del clients[client_id]
        else:
            print('No existe el cliente con el ID', client_id)
    if option == '3':
        client_id = input('Introduce ID del cliente: ')
        if client_id in clients:
            print('ID:', client_id)
            for key, value in clients[client_id].items():
                print(key.title() + ':', value)
        else:
            print('No existe el cliente con el ID', client_id)
    if option == '4':
        print('Lista de clientes')
        for key, value in clients.items():
            print(key, value['name'])
    if option == '5':
        print('Lista de clientes preferentes')
        for key, value in clients.items():
            if value['preferente']:
                print(key, value['name'])
    option = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')
