class Rectangle:
   
   # __bool__, __str__, __eq__
   # dunder init
   #constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
r1 = Rectangle(width=3, height=5)
print(r1.area())

r2 = Rectangle(width=5, height=4)
print(r2.area())