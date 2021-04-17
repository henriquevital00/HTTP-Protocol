from socket import *
import sys
import os

HOST = ''
PORT = 10000


def createServer():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(5)
        conn, addr = sock.accept()

        print("Conectado por {} na porta {}".format(addr[0], addr[1]))
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type: text/html; charset=utf-8\r\n"
        data += "\r\n"
        data += "<html><body>Hello World!</body></html>\r\n\r\n"
        conn.send(data.encode())

        #try:
        #    while True:
        #        data = sock.recv(1024).decode()
        #        print("Finalizando conexao do cliente", addr)
        #        print("Access http://localhost:10000")

        #except Exception as e:
        #    print(e)
        #    print("Deu ruim emu irmao")
        sock.close()


createServer()
