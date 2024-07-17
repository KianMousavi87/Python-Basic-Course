x = [1, 2, 3]
print(id(x))

y = [1, 2, 3]
print(id(y))
print(x == y)
print(x is y)

y = None
print(y is None)
print(id(y))
x = y
print(x is y)
print(x == y)