class Rectangle:
    # metnod
    def perimeter(self):
        return f"perimeter, {id(self)}"
    def area(self, name):
        print(name)
        return f"area, {id(self)}"
    
r1 = Rectangle()
r2 = Rectangle()
print(r1.area("rectangle 1"), id(r1))
print(r2.area("rectangle 2"), id(r2))
print(r2.perimeter())