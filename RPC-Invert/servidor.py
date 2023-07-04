import rpyc

class StringService(rpyc.Service):
    def on_connect(self, conn):
        print("Conexão estabelecida.")

    def on_disconnect(self, conn):
        print("Conexão encerrada.")

    def exposed_reverse_string(self, text):
        return text[::-1]

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(StringService, port=12345)
    server.start()
