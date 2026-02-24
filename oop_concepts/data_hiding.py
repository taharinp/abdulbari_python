class Parent:
    def __init__(self, d):
        self.data=d
    def show(self):
        print(self.data)
p=Parent(10)
p.show()
p.data=20
p.show()


#