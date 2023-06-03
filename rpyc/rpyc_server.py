
import rpyc
from rpyc.utils.server import ThreadedServer


@rpyc.service
class TestService(rpyc.Service):
    @rpyc.exposed
    def valueReturn(self, data):
        return data


print('starting server')
server = ThreadedServer(TestService, port=18811)
server.start()
