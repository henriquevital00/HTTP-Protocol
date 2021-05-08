from abc import ABC
from utils.functions import HttpDateTime

class Response(ABC):

    def __init__(self, method, url):
        self.method = method
        self.url = url
        self.status = None
        self.data = None

    def ResponseHandler(self, data, content_type, isFileMoved = False, newFilePath = None):

        header = "HTTP/1.1 200 OK\r\n"

        if isFileMoved:
            header = "HTTP/1.1 302 Found\r\n"
            header += "Location: /{}\r\n".format(newFilePath)

        header += "Content-Type: {}\r\n".format(content_type)
        header += "Date: {}\r\n".format(HttpDateTime())
        header += "Content-Length: {}\r\n".format(len(data.encode("utf-8")))
        header += "Connection: close\r\n\r\n"
        header += data if not isFileMoved else ""
        header += "\r\n\r\n"

        return header


    def BinaryResponseHandler(self, data, size, content_type, isFileMoved = False, newFilePath = None):

        http_binary_file_headers = "HTTP/1.1 200 OK\r\n"

        if isFileMoved:
            http_binary_file_headers = "HTTP/1.1 302 Found\r\n"
            http_binary_file_headers += "Location: {}\r\n".format(newFilePath)

        http_binary_file_headers += "Content-Type: {}\r\n".format(content_type)
        http_binary_file_headers += "Content-Length: {}\r\n".format(size)
        http_binary_file_headers += "Accept-Ranges: bytes\r\n\r\n"

        return [http_binary_file_headers, data]


