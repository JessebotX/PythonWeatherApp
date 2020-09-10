class DataModel:
    def __init__(self):
        self.temp_k = None
        self.temp_c = None
        self.temp_f = None

    @property
    def temp_k(self):
        return self.temp_k

    @temp_k.setter
    def temp_k(self, value):
        self.temp_k = value

    @property
    def temp_c(self):
        return self.temp_c

    @temp_c.setter
    def temp_c(self, value):
        self.temp_c = value

    @property
    def temp_f(self):
        return self.temp_f

    @temp_f.setter
    def temp_f(self, value):
        self.temp_f = value
        


def testing():
    """
    Test data model module
    """
    print("Hello World")