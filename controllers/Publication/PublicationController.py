import json

class PublicationController:

    def __init__(self):
        self.file_name = 'controllers/Publication/publications.json'


    def create(self, sent_data):
        with open(self.file_name, "r+") as file:
            data = json.load(file)
            sent_data = json.loads(sent_data)
            sent_data["id"] = data[-1]["id"] + 1
            data.append(sent_data)
            file.seek(0)
            json.dump(data, file, indent=4)
            return json.dumps(data)

    def findById(self, id):
        try:
            with open(self.file_name, 'r') as json_file:
                data = json.load(json_file)
                for publication in data:
                    if publication["id"] == id:
                        return publication
        except:
            print('Error searching in json file')

    def findAll(self):
        with open(self.file_name, 'r+') as file:
            data = json.load(file)
            file.seek(0)

            return json.dumps(data)

    def deleteById(self, id):
        with open(self.file_name, "r+") as file:
            data = json.load(file)
            for idx, publication in enumerate(data):
                if publication["id"] == id:
                    data.pop(idx)
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    return json.dumps(data)


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




