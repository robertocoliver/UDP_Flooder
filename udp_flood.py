import socket

address = ('127.0.0.1', 8000)

def conexao():
        cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return cliente

def enviando(cliente):
    try:
        while True:
            
            msg = 'sending a request' + '\n'
            data = cliente.sendto(msg.encode(), address)

    except Exception as error:
        print(f'{error}')
