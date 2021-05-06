import os
from resources.HttpResponses.HttpResponse import Response
from resources.HttpExceptions.NotFoundException import NotFoundException
from utils.StaticFilesConstants import *
from resources.HttpEndpoints.AppEndpoints import endpoints
from resources.HttpEndpoints.EndpointFactory import Endpoint
from resources.HttpHeaders.ContentTypes import MIME_content_types as content_types


class HTTP_Get(Response):

    def __init__(self, method, url):
        super().__init__(method, url)
        self.content_type = ''
        self.getResource()


    def getResource(self):

        endpoint = Endpoint(self.url)

        if not endpoint.isStaticFileRequested:
            self.content_type = "application/json"

            try:
                id = int(endpoint.lastPathLink)
                self.data = self.ResponseHandler(endpoints["GET"]["/".join(endpoint.splitPath[0:-1])](id), self.content_type)

            except Exception:
                self.data = self.ResponseHandler(endpoints["GET"][self.url](), self.content_type)

        else:

            if self.url == "/":
                self.url = "/index.html"

            self.url = "static" + self.url #file path

            try:

                requestedFileOpen = None

                if endpoint.fileExtension[-1] not in page_script_extensions :
                    requestedFileOpen = open(self.url, "rb")
                else:
                    requestedFileOpen = open(self.url, "r", encoding="utf-8")


                with requestedFileOpen as content:

                    file_content = content.read()

                    self.content_type = content_types[endpoint.fileExtension[-1]]

                    if endpoint.fileExtension[-1] in page_script_extensions:
                        self.data = self.ResponseHandler(file_content,self.content_type)
                    else:
                        binaryFileSize = os.stat(self.url).st_size
                        self.data = self.BinaryResponseHandler(file_content, binaryFileSize)

            except FileNotFoundError as ex:
                self.data = NotFoundException(str(ex)).data



    def BinaryResponseHandler(self, data, size):

        http_image_headers = "HTTP/1.1 200 OK\r\n"
        http_image_headers += "Content-Type: {}\r\n".format(self.content_type)
        http_image_headers += "Content-Length: {}\r\n".format(size)
        http_image_headers += "Accept-Ranges: bytes\r\n\r\n"

        return [http_image_headers, data]