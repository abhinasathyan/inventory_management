class Country:
    def __init__(self, name=None,ipod_num=None,price=None):
        self.name=name
        self.ipod_num=ipod_num
        self.price=price
    def getCountry(self):
        return self.name