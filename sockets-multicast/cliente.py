import socket

# Função que envia a mensagem para o servidor multicast
def send_message(multicast_address, multicast_port, message):
    # Criação do socket multicast
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Configura o socket para utilizar multicast
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    
    # Envia a mensagem para o grupo multicast
    sock.sendto(message.encode(), (multicast_address, multicast_port))
    
    # Fecha o socket
    sock.close()

if __name__ == '__main__':
    # Define o endereço e a porta do servidor multicast
    multicast_address = 'localhost'
    multicast_port = 5000
    
    # Pede ao usuário para digitar uma mensagem
    message = input('Digite a mensagem que será enviada para o servidor: ')
    
    # Envia a mensagem para o servidor multicast
    send_message(multicast_address, multicast_port, message)
