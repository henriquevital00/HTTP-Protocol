from resources.HttpResponses.HttpDelete import HTTP_Delete
from resources.HttpResponses.HttpGet import HTTP_Get
from resources.HttpResponses.HttpPost import HTTP_Post

class ResponseFactory:

    def __init__(self):
        pass

    @staticmethod
    def InstanceResponse(method, url, data):
        if method == "POST":
            return HTTP_Post(method, url, data)
        elif method == "GET":
            return HTTP_Get(method, url)
        elif method == "DELETE":
            return HTTP_Delete(method, url)
