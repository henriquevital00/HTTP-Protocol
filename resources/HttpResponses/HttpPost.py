from resources.HttpResponses.HttpResponse import Response

class HTTP_Post(Response):

    def __init__(self, method, url, data):
        super().__init__(self, method, url, data)
        sent_data = data
