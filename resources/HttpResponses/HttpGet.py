import base64
from resources.HttpResponses.HttpResponse import Response
from resources.HttpExceptions.NotFoundException import NotFoundException


class HTTP_Get(Response):
    def __init__(self, method, url):
        super().__init__(method, url)
        self.content_type = ''  # TRATAR PARA HTML, IMAGEM E RETORNO DE REGISTRO (JSON)
        self.requestedDataType()

    def requestedDataType(self):
        referencedFile = self.url.split("/")[-1]
        fileExtension = referencedFile.split(".")
        isStaticFileRequested = len(fileExtension) > 1

        if not isStaticFileRequested:
            self.content_type = "application/json"
        else:
                if fileExtension[-1] == "html":
                    self.content_type = "text/html"
                else:
                    self.content_type = 'image/' + fileExtension[-1]

                if self.url in ["/"]:
                    self.url = "/index.html"

                self.url = "../static" + self.url

                try:
                    openMethod = "rb" if fileExtension[-1] != "html" else "r"

                    with open(self.url, openMethod) as content:

                        file_content = content.read()

                        if fileExtension[-1] != "html":
                            file_content = base64.b64encode(file_content)
                            file_content = str(base64.b64decode(file_content))[2:-1]

                        self.data = self.ResponseHandler(file_content,
                                                         self.content_type)

                except Exception as ex:
                    print(ex)
                    self.data = NotFoundException().ResponseHandler()