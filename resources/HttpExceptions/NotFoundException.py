from resources.HttpExceptions.HttpException import HTTP_Exception


class NotFoundException(HTTP_Exception):

    def __init__(self):
        super().__init__("404", "NOT FOUND")




