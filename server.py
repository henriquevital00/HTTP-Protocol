from socket import *
import sys
import os


class Server(object):
    def __init__(self):
        self.HOST = ''
        self.PORT = 9000

    def createServer(self):
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.bind((self.HOST, self.PORT))
            sock.listen(5)
            while True:
                conn, addr = sock.accept()
                print("Conectado por {} na porta {}".format(addr[0], addr[1]))
                pid = os.fork()
                if pid == 0:
                    data = "HTTP/1.1 200 OK\r\n"
                    data += "Content-Type: text/html; charset=utf-8\r\n"
                    data += "\r\n"
                    data += "<html><body>Hernique fala y  fala!</body></html>\r\n\r\n"
                    conn.send(data.encode())
                else:
                    conn.close()
