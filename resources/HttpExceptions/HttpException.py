from resources.HttpResponses.HttpResponse import Response

class HTTP_Exception(Response):
    def __init__(self, status, phrase):
        self.status = status
        self.phrase = phrase

    def ResponseHandler(self):
        return ("HTTP/1.1 {0} {1}\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "\r\n"
                "<html>"
                "<body>"
                "<h1>ERROR {2}</h1>"
                "</body>"
                "</html>"
                "\r\n\r\n".format(self.status, self.phrase, self.status))
