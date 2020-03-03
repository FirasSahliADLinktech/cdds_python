from .runtime import Runtime
from .dds_binding import *
import jsonpickle

from pydds import *

class FlexyWriter:
    def __init__(self, pub, flexy_topic, ps = None):
        self.rt = Runtime.get_runtime()
        self. prticipant= pub.participant
        self.qos = self.rt.to_rw_qos(ps)
        self.handle = self.rt.ddslib.dds_create_writer(pub.handle, flexy_topic.topic, self.qos, None)

        assert (self.handle > 0)
        self.keygen = flexy_topic.gen_key

    def write(self, s):
        gk = self.keygen(s)
        kh = KeyHolder(gk)
        key = jsonpickle.encode(kh)
        value = jsonpickle.encode(s)
        sample = DDSKeyValue(key.encode(), value.encode())
        self.rt.ddslib.dds_write(self.handle, byref(sample))

    def write_all(self, xs):
        for x in xs:
            self.write(x)

    def dispose_instance(self, s):
        gk = self.keygen(s)
        kh = KeyHolder(gk)
        key = jsonpickle.encode(kh)
        value = jsonpickle.encode(s)
        sample = DDSKeyValue(key.encode(), value.encode())
        self.rt.ddslib.dds_dispose(self.handle, byref(sample))