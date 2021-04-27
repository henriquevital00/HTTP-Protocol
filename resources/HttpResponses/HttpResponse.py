from abc import ABC

class Response(ABC):
    def __init__(self, method, url):
        self.method = method
        self.url = url
        self.status = ''
        self.data = ''

    def ResponseHandler(self, data, content_type):
        header = "HTTP/1.1 200 OK\r\n"
        header += "Content-Type: {}\r\n".format(content_type)
        header += "\r\n"
        header += data
        header += "\r\n\r\n"

        return header



