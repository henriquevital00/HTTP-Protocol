import json

class PublicationController:

    def __init__(self):
        self.file_name = 'controllers/Publication/publications.json'


    def create(self, data):
        pass

    def findById(self, id):
        with open(self.file_name, 'r') as json_file:
            data = json.load(json_file)
            return data[str(id)][2:-2]

    def findAll(self):
        with open(self.file_name, 'r') as json_file:
            return str(json.load(json_file))[2:-2]


    def removeData(self, Id: str) -> None:
        try:
            with open(self.file_name, 'r') as data_file:
                data = json.load(data_file)
            if Id in data:
                del data[Id]
            with open(self.file_name, 'w') as data_file:
                data = json.dump(data, data_file)
        except:
            print("Can not remove postagem")


    def searchData(self, Id: str) -> None:
        try:
            with open(self.file_name, 'r') as json_file:
                data = json.load(json_file)
                return {'text': data[Id]['text'], 'image': data[Id]['image']}
        except:
            print('Error searching in json file')


    def appendData(self, Id: str, text: str, image: str) -> None:
        file_data = {}
        try:
            with open(self.file_name, 'r') as json_file:
                file_data = json.load(json_file)
        except IOError:
            print("File not accessible")
        finally:
            with open(self.file_name, 'w') as json_file:
                file_data[Id] = {'text': text, 'image': image}
                json.dump(file_data, json_file)
