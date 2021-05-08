from enum import Enum

class Endpoint:


    def __init__(self, url):

        self.splitPath = url.split('/')
        self.lastPathLink = self.splitPath[-1]

        self.referencedFile = self.lastPathLink if url != '/' else '/'
        self.fileExtension = self.referencedFile.split(".")

        self.isStaticFileRequested = len(self.fileExtension) > 1 or self.fileExtension[-1] == "/"







