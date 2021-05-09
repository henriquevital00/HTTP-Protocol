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
                data = self.recv_all(conn)

                try:

                    builder = HttpBuilder(data.decode())
                    result_data = builder.result().data

                    print('\nRequest Result')  # just for output test, will be removed later
                    print(data.decode())

                    print('\nResponse Result')  # just for output test, will be removed later

                    if isBinaryData(result_data):

                        headers, binaryContent = (result_data[0], result_data[1])

                        print(headers + str(binaryContent))  # just for output test, will be removed later

                        conn.send(headers.encode())
                        conn.send(binaryContent)
                        conn.close()
                    else:
                        print(result_data)  # just for output test, will be removed later
                        conn.sendall(result_data.encode())
                        conn.close()

                except Exception:
                    conn.close()

    def recv_all(self, conn):
        k: int = 1
        buffer: int = 128
        chunk = header = conn.recv(buffer)
        end_msg_str = b'\r\n\r\n'
        body = b''
        diff: int = 0
        loop_control = recv_control = True

        while loop_control:
            k += 1
            end_msg_counter: int = 0
            str_chunk = chunk.decode()

            for index in range(len(str_chunk)):

                end_msg_counter = end_msg_counter + 1 if str_chunk[index] == '\r' or str_chunk[index] == '\n' else 0

                if end_msg_counter == 4 or len(chunk) < buffer:
                    diff = len(chunk) - index
                    recv_control = loop_control = False
                    break

            if recv_control:
                chunk = conn.recv(buffer)
                header += chunk

        content_length = self.get_content_length(header)

        if content_length > 0:
            body = self.recv_body(conn, content_length, diff)

        return header + body


    def get_content_length(self, header):
        header = str(header)
        h = header.split(':')

        for i in range(len(h)):

            if 'content-length' in h[i].lower():
                temp = ''
                for byte in range(len(h[i+1])):

                    if h[i+1][byte].isnumeric():
                        temp += h[i+1][byte]

                cl = int(temp)

                return cl

        return 0

    def recv_body(self, conn, content_length, diff):

        body = b''
        buffer = 256
        chunk = b''

        if content_length > diff:
            chunk = conn.recv(buffer)

            while True:

                body += chunk
                if len(body) == content_length or len(chunk) < buffer:
                    break
                chunk = conn.recv(buffer)

        return body