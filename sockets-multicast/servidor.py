import socket

# Função que pega as informações do cliente
def get_response():
    while True:
        message, client_address = multicast_socket.recvfrom(1024)
        message_str = message.decode()
        
        geted_data = [client_address, message_str]
        
        return geted_data

# Função que inverte a mensagem
def invert_message(message):
    return message[::-1]

# Função que manipula as informações e envia a resposta ao grupo multicast
def send_response():
    params = get_response()
    
    client_address = params[0]
    message_str = params[1]
    
    inverted_str = invert_message(message_str)

    print(f'Mensagem recebida "{inverted_str}" do IP {client_address}')

    multicast_socket.sendto(inverted_str.encode(), client_address)

if __name__ == '__main__':
    # Criando o socket multicast
    multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    # Torna disponível o endereço e a porta
    multicast_socket.bind(('localhost', 5000))

    print('Aguardando conexão do client...')
    
    send_response()
