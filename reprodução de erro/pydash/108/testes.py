class Test(object):
    @property
    def blah(self):
        return 5


test = 4

a = getattr(test, '__dict__', {})
print(dir(test))
print("TESTE: ", vars(a))