from resources.HttpResponses.HttpResponse import Response
from resources.HttpEndpoints.AppEndpoints import endpoints

class HTTP_Post(Response):

    def __init__(self, method, url, data):
        super().__init__(method, url)
        self.sent_data = data
        self.sendRequestedData()

    def sendRequestedData(self):
        self.content_type = "application/json"
        self.data = self.ResponseHandler(endpoints["POST"][self.url](self.sent_data), self.content_type)

