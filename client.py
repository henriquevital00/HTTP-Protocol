from socket import *
from Gateway import HOST, PORT
from http import HTTP
from pdb import set_trace


class Client:
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((HOST, PORT))

    def sendMessage(self, data):
        self.sock.sendall(data.encode())

    def get_Index(self):

        with open("index.html") as content:
            data = content.read()
            self.sendMessage(HTTP.GET_Request(data))


def main():
    set_trace()
    client = Client()
    #client.get_Index()
    data = "HTTP/1.1 200 OK\r\n"
    data += "Content-Type: text/html; charset=utf-8\r\n"
    data += "\r\n"
    data += "<html><body>Hernique fala y  fala!</body></html>\r\n\r\n"
    client.sendMessage(data)


main()
