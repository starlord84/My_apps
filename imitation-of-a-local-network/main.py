class Server:
    
    servers = []

    def __init__(self):
        self.servers.append(self)
        self.ip = len(self.servers)
        self.buffer = []

    def send_data(self, data):
        self.router.buffer.append(data)

    def get_data(self):
        buffer_copy = self.buffer[:]
        self.buffer.clear()
        return buffer_copy

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.links = {}

    def link(self, server):
        self.links[server.ip] = server
        server.router = self

    def unlink(self, server):
        self.links[server.ip] = None

    def send_data(self):
        for data in self.buffer:
            if self.links[data.ip]:
                self.links[data.ip].buffer.append(data)
        self.buffer.clear()


class Data:

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
