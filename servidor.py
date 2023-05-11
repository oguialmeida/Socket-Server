import socket

# Função que pega as informções do cliente
def get_reponse():
    while True:
        message, client_address = comunic_socket.recvfrom(1024)
        message_str = message.decode()
        
        getedData = [client_address, message_str]
        
        return getedData

# Função que manipula as informações       
def send_reponse():
    params = get_reponse()
    
    client_address = params[0]
    message_str = params[1]
    
    inverted_str = message_str[::-1]

    print(f'Mensagem recebida "{message_str}"do IP {client_address}')

    comunic_socket.sendto(inverted_str.encode(), client_address)
    
if __name__ == '__main__':
    # Criando o socket de comunicação
    comunic_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Torna disponível o endereço e a porta
    comunic_socket.bind(('localhost', 5000))

    print('Aguardando conexão do client...')
    
    send_reponse()