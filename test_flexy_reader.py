__author__ = 'Angelo Corsaro'

from pydds import *
import time

# TODO: Factor out the definition of Vehicle position...
class VehiclePosition(FlexyTopic):
    def __init__(self, cid):
        super(FlexyTopic, self).__init__()
        self.x = 0
        self.y = 0
        self.key_ = cid

    def gen_key(self):
        return self.key_

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return 'VehiclePosition({0}, {1}, {2})'.format(self.key_, self.x, self.y)

def data_available(r):
    print('reader>> Listenerr Called!')
    samples = r.take(all_samples())
    for s in samples:
        if s[1].valid_data:
            print ('reader>> {0})'.format(s[0]))

def liveliness_changed(r, e):
    print(">>>>> Changed Liveliness!!")

def testDynaTypes():
    rt = Runtime()
    dp = Participant(0)

    t = FlexyTopic(dp,  'KeyValue')

    dr = FlexyReader(dp, t, None, [Reliable(), KeepLastHistory(10)])
    # dr.on_liveliness_changed(liveliness_changed)

    while True:
        samples = dr.read(all_samples())
        time.sleep(1)
        for s in samples:
            if s[1].valid_data:
                print("type(s[0]) = ", type(s[0]))
                print('reader>> {0})'.format(s[0]))
                

if __name__ == '__main__':
    testDynaTypes()
