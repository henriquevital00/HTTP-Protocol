import io, base64, chardet, json
from PIL import Image
from resources.HttpResponses.HttpResponse import Response
from resources.HttpExceptions.ExceptionsStatusCode import InternalServerError


class HTTP_Put(Response):

    def __init__(self, method, url, data):
        super().__init__(method, url)
        self.sent_data = data
        self.createFile()

    def createFile(self):

        byte = base64.b64decode(self.sent_data)
        detection = chardet.detect(byte)
        encoding = detection["encoding"]

        try:
            if encoding != None:

                with open('static/client-files/' + self.url, 'w') as file:
                    file.write(byte.decode(encoding))
                    self.data = self.ResponseHandler("", "", isFileCreated = True)
            else:
                img = Image.open(io.BytesIO(byte))
                img.save('static/client-files/' + self.url)

                self.data = self.ResponseHandler("", "", isFileCreated = True)

        except Exception as ex:

            errorOnCreateFile = json.dumps(
                {"error": "Error creating file on server: {}".format(str(ex))})

            self.data = InternalServerError(errorOnCreateFile).data
