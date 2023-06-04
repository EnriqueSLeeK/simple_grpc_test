
import rpyc
import classes as c
from rpyc.utils.server import ThreadedServer


@rpyc.service
class TestService(rpyc.Service):

    @rpyc.exposed
    def valueReturn(self, data):
        return c.genericObj(data)

    @rpyc.exposed
    def multiToOneReturn(self, data):
        return c.genericObj(data.data_0)


print('starting server')
server = ThreadedServer(TestService, port=18811,
                        protocol_config={"allow_public_attrs": True})
server.start()
