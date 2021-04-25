import os
from resources.HttpResponses.HttpResponse import Response
from resources.HttpExceptions.NotFoundException import NotFoundException
from utils.StaticFilesConstants import *
from utils.ApplicationEndpoints import endpoints

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

            isId = False
            id = 0


            try:
                id = int(lastPathLink)
                isId = True
            except Exception as ex: pass


            if isId:
                self.data = self.ResponseHandler(endpoints["GET"]["/".join(splitPath[0:-1])](id), self.content_type)
            else:
                self.data = self.ResponseHandler(endpoints["GET"][self.url](), self.content_type)

        else:
            if self.url == "/":
                self.url = "/index.html"

            self.url = "static" + self.url

            try:

                requestedFileOpen = None

                if  fileExtension[-1] not in page_script_extensions :
                    requestedFileOpen = open(self.url, "rb")
                else:
                    requestedFileOpen = open(self.url, "r", encoding="utf-8")


                with requestedFileOpen as content:

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