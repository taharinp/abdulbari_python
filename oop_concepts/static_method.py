class Rectangle:


      def __init__(self, l,b):
          self.l = l
          self.b = b

      def calc_area(l,b):
          return l*b

print(Rectangle.calc_area(10,5))