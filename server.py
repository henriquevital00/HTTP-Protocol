from socket import *
import sys
import os

HOST = '127.0.0.1'
PORT = 10000


def createServer():
    tcp = socket(AF_INET, SOCK_STREAM)
    tcp.bind((HOST, PORT))
    tcp.listen(1)

    print("O sevidor está pronto para receber!")

    while True:
        try:
            while (1):
                conn, addr = tcp.accept()
                pid = os.fork()
                if pid == 0:
                    now = datetime.now()
                    tcp.close()
                    print("Conectado por {} na porta {}".format(
                        addr[0], addr[1]))
                    data = conn.recv(2048)
                    data = "HTTP/1.1 200 OK\r\n"
                    data += "Content-Type: text/html; charset=utf-8\r\n"
                    data += "\r\n"
                    data += "<html><body>Hello World!</body></html>\r\n\r\n"
                    clientsocket.sendall(data.encode())
                    clientsocket.shutdown(SHUT_WR)
                    con.send(b'The server is off')
                    conn.close()
                    print("Finalizando conexao do cliente", addr)
                    print("Access http://localhost:9000")
                else:
                    conn.close()
        except:
            print("Deu ruim emu irmao")


createServer()
