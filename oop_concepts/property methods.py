class Rectangle:

    def __init__(self, l, b):
        self.l = l
        self.b = b
    @property
    def length(self):
        return self.l
    @length.setter
    def length(self, l):
        if l>=0:
            self.l = l
        else:
            self.l = l

r=Rectangle(10,6)
r.l=-8
print(r.length)