from resources.HttpExceptions.HttpException import HTTP_Exception


class NotFoundException(HTTP_Exception):

    def __init__(self, message):
        super().__init__("404", "NOT FOUND", message)

class InternalServerError(HTTP_Exception):

    def __init__(self, message):
        super().__init__("500", "Internal Server Error", message)




