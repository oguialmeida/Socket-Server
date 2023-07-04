import rpyc

class MathService(rpyc.Service):
    def on_connect(self, conn):
        print("Conexão estabelecida.")

    def on_disconnect(self, conn):
        print("Conexão encerrada.")

    def exposed_add_numbers(self, num1, num2):
        return num1 + num2

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(MathService, port=12345)
    server.start()
