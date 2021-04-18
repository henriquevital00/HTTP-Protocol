class HTTP():
    @staticmethod
    def GET_Response(data):
        header = "HTTP/1.1 200 OK\r\n"
        header += "Content-Type: text/html; charset=utf-8\r\n"
        header += "\r\n"
        header += data
        header += "\r\n\r\n"

        return header
