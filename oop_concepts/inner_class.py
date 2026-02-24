class Outer:

    def __init__(self):
        self.in_obj = self.Inner()

    def show(self):
        self.in_obj.show()

    class Inner:

        def __init__(self):
            self.idata = "inner data"

        def show(self):
            print(self.idata)


o = Outer()

o.show()