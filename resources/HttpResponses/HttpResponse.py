from abc import ABC
from utils.functions import HttpDateTime

class Response(ABC):

    def __init__(self, method, url):
        self.method = method
        self.url = url
        self.status = None
        self.data = None

    def ResponseHandler(self, data, content_type):
        header = "HTTP/1.1 200 OK\r\n"
        header += "Content-Type: {}\r\n".format(content_type)
        header += "Date: {}\r\n".format(HttpDateTime())
        header += "Last-Modified: Sun, 01 Jan 2021 22:04:35 GMT\r\n"
        header += "Content-Length: {}\r\n".format(len(data.encode("utf-8")))
        header += "Connection: close\r\n\r\n"
        header += data
        header += "\r\n\r\n"

        return header



