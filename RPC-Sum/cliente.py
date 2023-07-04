import rpyc

conn = rpyc.connect("localhost", 12345)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

result = conn.root.exposed_add_numbers(num1, num2)
print("Resultado da soma:", result)

conn.close()
