from abc import ABC
from utils.functions import HttpDateTime

class Response(ABC):
    def __init__(self, method, url):
        self.method = method
        self.url = url
        self.status = ''
        self.data = ''

    def ResponseHandler(self, data, content_type):
        header = "HTTP/1.1 200 OK\r\n"
        header += "Content-Type: {}; charset=ytf-8\r\n".format(content_type)
        header += "Date: {}\r\n".format(HttpDateTime())
        header += "Connection: Close\r\n\r\n"
        header += data
        header += "\r\n\r\n"

        return header



