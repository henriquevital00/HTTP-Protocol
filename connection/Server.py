from socket import *
from connection.Gateway import HOST, PORT
from resources.HttpResponses.HttpBuilder import HttpBuilder



class Server:
    def __init__(self):

        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.bind((HOST, PORT))
            sock.listen(5)

            while True:
                conn, addr = sock.accept()
                data = conn.recv(4024)
                print(data.decode())
                builder = HttpBuilder(data.decode())
                result_data = builder.getReponse().data
                print('Result')
                print(result_data)
                conn.sendall(result_data.encode())


def main():
    Server()


main()