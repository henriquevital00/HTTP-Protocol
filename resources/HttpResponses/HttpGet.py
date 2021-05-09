import os
from glob import iglob
from resources.HttpResponses.HttpResponse import Response
from resources.HttpExceptions.ExceptionsStatusCode import NotFoundException
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
                self.data = self.ResponseHandler(
                    endpoints["GET"]["/".join(endpoint.splitPath[0:-1])](id),
                    self.content_type)

            except Exception:
                self.data = self.ResponseHandler(endpoints["GET"][self.url](), self.content_type)

        else:

            if self.url == "/":
                self.url = "/index.html"

            try:
                currDir = os.path.abspath(os.curdir).replace("\\", "/")
                staticDirPath = currDir + "/static"

                fullPath = staticDirPath + self.url

                if os.path.exists(fullPath):
                    self.data = self.getFileContent(self.url,
                                                    endpoint.fileExtension[-1])
                    return

                else:

                    if endpoint.fileExtension[-1] == "/":
                        endpoint.lastPathLink = "index.html"

                    pathname = staticDirPath + "/**/" + endpoint.lastPathLink

                    for file in iglob(pathname, recursive=True):

                        file = file.replace("\\", "/")
                        filename = file.split("/")[-1]

                        if filename == endpoint.lastPathLink:
                            extension = "".join(filename.split(".")[1:])
                            self.data = self.getFileContent(
                                "".join(file.split("static/")[1:]),
                                extension,
                                isFileMoved=True,
                                newFilePath="/".join(file.split("/")[-2:]))
                            return

                raise FileNotFoundError

            except FileNotFoundError as ex:
                self.data = NotFoundException(str(ex)).data

    def getFileContent(self, url, fileExtension, isFileMoved=False, newFilePath=None):

        requestedFileOpen = None

        if fileExtension not in page_script_extensions:
            requestedFileOpen = open("static/" + url, "rb")
        else:
            requestedFileOpen = open("static/" + url, "r", encoding="utf-8")

        with requestedFileOpen as content:

            file_content = content.read()

            self.content_type = content_types[fileExtension]

            requestedFileOpen.close()

            if fileExtension in page_script_extensions:
                if not isFileMoved:
                    return self.ResponseHandler(file_content,
                                                self.content_type)
                else:
                    return self.ResponseHandler(file_content,
                                                self.content_type, isFileMoved,
                                                newFilePath)
            else:
                binaryFileSize = len(file_content)
                if not isFileMoved:
                    return self.BinaryResponseHandler(file_content, binaryFileSize,self.content_type)
                else:
                    return self.BinaryResponseHandler(file_content, binaryFileSize, self.content_type,
                                                      isFileMoved, newFilePath)