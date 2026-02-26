class parent:
    def show(self):
        print('parent show')it

class child(parent):
    def show(self):
        print('child show')

c=child()
c.show()