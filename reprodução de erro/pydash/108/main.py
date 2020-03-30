import pydash

class Test(object):
    @property
    def blah(self):
        return 5


test = Test()

print(pydash.pick(test, 'blah'))


class Test(object):
    def __init__(self):
        self.blah = 5


test = Test()

print(pydash.pick(test, 'blah'))
