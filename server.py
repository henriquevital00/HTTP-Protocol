from socket import *
from Gateway import HOST, PORT
from http import HTTP
from pdb import set_trace


class Server:
    def __init__(self):
        pass

    def get_page(self, page):
        try:
            with open(page) as content:
                data = content.read()
                return HTTP.GET_Response(data)
        except Exception as e:
            print("Deu merda parceiro")

    def parse_request(self, data):
        return data.split(' ')[1][1:]

    def test(self):
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.bind((HOST, PORT))
            sock.listen(5)
            while True:
                conn, addr = sock.accept()
                data = conn.recv(4024)
                print(data.decode())
                page = self.parse_request(data.decode())
                print("PAGE: ", page)
                data = self.get_page(page)
                conn.sendall(data.encode())


def main():
    server = Server()
    server.test()


main()
