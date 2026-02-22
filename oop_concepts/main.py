class Rectangle:


    def __init__(self, width, height):
        self.l=10
        self.b=15



    def area(self):
        return self.l*self.b
    def perimeter(self):
        return self.l+self.b

r=Rectangle(5,5)
print(r.area())
print(r.perimeter())
