from socket import *
import sys
import os

HOST = ''
PORT = 10000


def createServer():
    tcp = socket(AF_INET, SOCK_STREAM)
    tcp.bind((HOST, PORT))
    tcp.listen(1)

    print("O sevidor está pronto para receber!")

    try:
        while True:
            conn, addr = tcp.accept()
            pid = os.fork()
            if pid == 0:
                tcp.close()
                print("Conectado por {} na porta {}".format(addr[0], addr[1]))
                data = "HTTP/1.1 200 OK\r\n"
                data += "Content-Type: text/html; charset=utf-8\r\n"
                data += "\r\n"
                data += "<html><body>Hello World!</body></html>\r\n\r\n"
                conn.sendall(data.encode())
                conn.shutdown(SHUT_WR)
                conn.send(b'The server is off')
                conn.close()
                print("Finalizando conexao do cliente", addr)
                print("Access http://localhost:9000")
            else:
                conn.close()
    except Exception as e:
        print(e)
        print("Deu ruim emu irmao")
        conn.close()


createServer()
