import json

class PublicationController:

    def __init__(self):
        self.file_name = 'controllers/Publication/publications.json'


    def create(self, sent_data):
        with open(self.file_name, "r+") as file:
            data = json.load(file)
            sent_data = json.loads(sent_data)
            sent_data["id"] = data[-1]["id"] + 1 if len(data) > 0 else 1
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
        try:
            with open(self.file_name, 'r+') as data_file:
                data = json.load(data_file)

                for i in range(len(data)):
                    if data[i]['id'] == id:
                        del data[i]
                        break

                data_file.seek(0)
                data_file.truncate(0)

                json.dump(data, data_file, indent=4)

                return json.dumps(data)

        except:
            print("Can not remove postagem")