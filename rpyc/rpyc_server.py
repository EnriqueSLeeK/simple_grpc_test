
import rpyc
from rpyc.utils.server import ThreadedServer


class integerOne:
    def __init__(self, data):
        self.data = data


@rpyc.service
class TestService(rpyc.Service):
    @rpyc.exposed
    def valueReturn(self, data):
        return data

    @rpyc.exposed
    def multiToOneReturn(self, data):
        # It will create a new instance of a class
        return self.integerOne(data[0])


print('starting server')
server = ThreadedServer(TestService, port=18811)
server.start()
