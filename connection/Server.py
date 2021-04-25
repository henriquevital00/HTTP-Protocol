from socket import *
from .Gateway import HOST, PORT
from resources.HttpResponses.HttpBuilder import HttpBuilder
from utils.functions import isBinaryData


class Server:
    def __init__(self):

        with socket(AF_INET, SOCK_STREAM) as sock:

            sock.bind((HOST, PORT))
            sock.listen(5)
            print("Listening at {}:{}".format(HOST, PORT))

            while True:
                conn, addr = sock.accept()
                data = conn.recv(4096)

                # Browser request
                print(data.decode()) # just for output test, will be removed later

                builder = HttpBuilder(data.decode())
                result_data = builder.result().data

                print('Result') # just for output test, will be removed later

                if isBinaryData(result_data):

                    headers, binaryContent = (result_data[0], result_data[1])

                    print(headers + str(binaryContent)) # just for output test, will be removed later

                    conn.send(headers.encode())
                    conn.send(binaryContent)
                else:

                    print(result_data)  # just for output test, will be removed later

                    conn.sendall(result_data.encode())
