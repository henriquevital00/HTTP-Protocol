from resources.HttpResponses.HttpResponse import Response
from utils.functions import HttpDateTime

class HTTP_Exception(Response):

    def __init__(self, status, phrase, message):
        self.status = status
        self.phrase = phrase
        self.message = message
        self.data = self.ResponseHandler()


    def ResponseHandler(self):

        return ("HTTP/1.1 {} {}\r\n"
                "Content-Type: application/json\r\n"
                "Date: {}\r\n"
                "Content-Length: {}\r\n"
                "\r\n"
                "{}"
                "\r\n\r\n".format(self.status, self.phrase, HttpDateTime(), len(self.message.encode("utf-8")), self.message))
