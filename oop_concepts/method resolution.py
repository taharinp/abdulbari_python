class Parent:
    def show(self):
        print ('parent show')

class child(Parent):
    def show(self):
        print ('child show')

c=child()
c.show()
print(child.mro())