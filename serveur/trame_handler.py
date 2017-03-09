import afficheur
class DataHandler:

    def __init__(self, data):
        self.data = data
        self._aff()
        self._identify()

    def _aff(self):
        print(self.data)
        print(self.data[0])

    def _identify(self):
        if self.data[0] == 0x10:
            print("ok")
            print(self.data[1:])
            aff = afficheur.Afficheur("192.168.15.10", 502)
            aff.msg(self.data[1:])



