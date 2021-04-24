import os
from resources.HttpResponses.HttpResponse import Response
from resources.HttpExceptions.NotFoundException import NotFoundException
from utils.StaticFilesConstants import *

class HTTP_Get(Response):

    def __init__(self, method, url):
        super().__init__(method, url)
        self.content_type = ''
        self.requestedDataType()

    def requestedDataType(self):

        splitPath = self.url.split('/')
        lastPathLink = splitPath[-1]

        referencedFile = lastPathLink if self.url != '/' else '/'
        fileExtension = referencedFile.split(".")

        isStaticFileRequested = len(fileExtension) > 1 or fileExtension[-1] == "/"

        if not isStaticFileRequested:
            self.content_type = "application/json"
        else:

            if self.url == "/":
                self.url = "/index.html"

            self.url = "static" + self.url

            try:
                openMethod = "rb" if fileExtension[-1] not in page_script_extensions else "r"

                with open(self.url, openMethod) as content:

                    file_content = content.read()

                    if fileExtension[-1] in page_script_extensions:
                        self.content_type = 'text/'

                        if fileExtension[-1] == "/":
                            self.content_type += "html"
                        elif fileExtension[-1] == "js":
                            self.content_type += "javascript"
                        else:
                            self.content_type += fileExtension[-1]

                        self.data = self.ResponseHandler(file_content,self.content_type)
                    else:
                        self.content_type = 'image/'
                        self.content_type += fileExtension[-1] if fileExtension[-1] != "ico" else "x-icon"
                        imgSize = os.stat(self.url).st_size
                        self.data = self.BinaryResponseHandler(file_content, imgSize)

            except FileNotFoundError as ex:
                self.data = NotFoundException().ResponseHandler()

            except Exception as ex:
                print(ex)


    def BinaryResponseHandler(self, data, size):

        http_image_headers = "HTTP/1.1 200 OK\r\n"
        http_image_headers += "Content-Type: {}\r\n".format(self.content_type)
        http_image_headers += "Content-Length: {}\r\n".format(size)
        http_image_headers += "Accept-Ranges: bytes\r\n\r\n"

        return [http_image_headers, data]