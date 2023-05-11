import socket

# Cria um objeto socket UDP
def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envia mensagem para o servidor
def send_message(sock, server_address, message):
    sock.sendto(message.encode(), server_address)

 # Recebe a mensagem invertida do servidor
def receive_message(sock):
    inverted_message, server_address = sock.recvfrom(1024)
    return inverted_message.decode()

# Fecha o socket
def close_socket(sock):
    sock.close()
    
if __name__ == '__main__':
    # Cria um objeto socket UDP
    comunic_socket = create_socket()

    # Define o endereço do servidor
    server_address = ('localhost', 5000)

    # Pede ao usuário para digitar uma mensagem
    message = input('Digite a mensagem que será invertida: ')

    # Envia a mensagem para o servidor
    send_message(comunic_socket, server_address, message)

    # Recebe a mensagem invertida do servidor
    inverted_message_str = receive_message(comunic_socket)

    # Imprime a mensagem invertida recebida
    print(f'Mensagem invertida recebida: {inverted_message_str}')

    # Fecha o socket
    close_socket(comunic_socket)
