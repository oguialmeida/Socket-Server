import rpyc

conn = rpyc.connect("localhost", 12345)

message = input("Digite uma mensagem: ")
reversed_message = conn.root.exposed_reverse_string(message)
print("Mensagem invertida:", reversed_message)

conn.close()
