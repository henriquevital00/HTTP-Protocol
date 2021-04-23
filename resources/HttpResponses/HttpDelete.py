from resources.HttpResponses.HttpResponse import Response


class HTTP_Delete(Response):

    def __init__(self, method, url):
        super().__init__(self, method, url)

