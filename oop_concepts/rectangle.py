class Rectangle:
    count=0


    def __init__(self, width, height):
        self.l=10
        self.b=15



    def area(self):
        return self.l*self.b
    def perimeter(self):
        return self.l+self.b

r1=Rectangle(5,5)
print('r1 id:' , id(r1))
print(r1.area())
print(r1.perimeter())



