from resources.HttpResponses.HttpResponse import Response
from utils.ApplicationEndpoints import endpoints

class HTTP_Delete(Response):

    def __init__(self, method, url):
        super().__init__(self, method, url)
        self.deleteData()

    def deleteData(self):
        splitPath = self.url.split('/')
        self.content_type = "application/json"

        self.data = self.ResponseHandler(endpoints["DELETE"]["/".join(splitPath[0:-1])](id), self.content_type)

