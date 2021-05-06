


class EndpointBuilder:

    def __init__(self, url):
        splitPath = url.split('/')
        lastPathLink = splitPath[-1]

        referencedFile = lastPathLink if url != '/' else '/'
        fileExtension = referencedFile.split(".")

        self.isStaticFileRequested = len(fileExtension) > 1 or fileExtension[-1] == "/"

    def getResourceType(self):
        return self.isStaticFileRequested






