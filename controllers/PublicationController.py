import json

# JSON genérico, especificar depois para cada model
class CreateJson:

    def _init_(self):
        pass

    def appendData(self, Id, data):
        with open("publications.json", 'r+') as json_file:
            file_data = json.loads(json_file)
            file_data.update(str(Id), {'text': data})
            json_file.seek(0)
            json.dump(file_data, json_file)

    def removeData(self, Id):
        with open('publications.json', 'r') as data_file:
            data = json.load(data_file)
        if str(Id) in data:
            del Id
        with open('publications.json', 'w') as data_file:
            data = json.dump(data, data_file)

    def searchData(self, Id):
        with open('publications.json', 'r') as json_file:
            data = json.load(json_file)
            return data[str(Id)]['text']