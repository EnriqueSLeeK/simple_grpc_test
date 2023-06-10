
import rpyc

conn = rpyc.connect('localhost', 18811,
                    config={"allow_public_attrs": True})

conn.root.shutdown()
