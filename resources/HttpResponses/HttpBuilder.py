from resources.HttpResponses.HttpFactory import ResponseFactory


class HttpBuilder:
    def __init__(self, received_data):
        self.received_data = received_data.split("\r\n\r\n")[-1]
        self.method = received_data.split(' ')[0]
        self.url = received_data.split(' ')[1]

    def result(self):
        return ResponseFactory.InstanceResponse(self.method, self.url,
                                                self.received_data)

