import os, glob, json
from resources.HttpEndpoints.EndpointFactory import Endpoint
from resources.HttpResponses.HttpResponse import Response
from resources.HttpEndpoints.AppEndpoints import endpoints
from resources.HttpExceptions.NotFoundException import NotFoundException


class HTTP_Delete(Response):

    def __init__(self, method, url):
        super().__init__(method, url)
        self.deleteData()

    def deleteData(self):

        endpoint = Endpoint(self.url)

        if not endpoint.isStaticFileRequested:

            id = int(endpoint.splitPath[-1])
            self.content_type = "application/json"
            self.data = self.ResponseHandler(endpoints["DELETE"]["/".join(endpoint.splitPath[0:-1])](id),
                                             self.content_type)

        else:

            self.content_type = "application/json"
            successOnDelete = json.dumps({"message": "Deleted '{}' sucessfully!".format(endpoint.lastPathLink)})
            notFoundOnDelete = json.dumps(
                {"error": "The requested file '{}' was not found on this server".format(endpoint.lastPathLink)})

            try:
                currDir = os.path.abspath(os.curdir).replace("\\", "/")
                staticDirPath = currDir + "/static/"

                fullPath = staticDirPath + self.url

                if os.path.exists(fullPath):
                    os.remove(fullPath)
                    self.data = self.ResponseHandler(successOnDelete, self.content_type)
                    return

                else:
                    pathname = staticDirPath + "**/" + endpoint.lastPathLink
                    for file in glob.iglob(pathname, recursive=True):
                        file = file.replace("\\", "/")
                        filename = file.split("/")[-1]

                        if filename == endpoint.lastPathLink:
                            os.remove(file)
                            successMovedFile = json.dumps(
                                {
                                    "message": "Deleted '{}' sucessfully!".format(endpoint.lastPathLink),
                                    "log": "This file was moved! New folder: '{}'".format(file.split("/")[-2])
                                }, indent=4
                            )
                            self.data = self.ResponseHandler(successMovedFile, self.content_type)
                            return

                raise FileNotFoundError

            except FileNotFoundError:

                self.data = NotFoundException(notFoundOnDelete).data




