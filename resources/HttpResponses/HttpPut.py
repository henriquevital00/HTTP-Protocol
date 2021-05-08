import os
import io
from PIL import Image
from resources.HttpResponses.HttpResponse import Response

class HTTP_Put(Response):
    def init(self, method, url):
        super().__init__(method, url)

    def readimage(self, path):
        count = os.stat(path).st_size / 2
        print(f'count ===  {count}')
        with open(path, "rb") as f:
            return bytearray(f.read())

    def create_image(self, fileName ,data):
        path = f'/static/{fileName}'
        if isinstance(data, bytearray):
            extension = '.jpeg'
            bytes = self.readimage(path + extension)
            image = Image.open(io.BytesIO(bytes))
            image.save(path)
            #self.data = bytes