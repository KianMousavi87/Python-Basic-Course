def compute_add_sub(a, b):
    return a + b, a - b

print(compute_add_sub(2, 3))

t = (1, 2, 3)
print(id(t))
x = [1, 2, 3]
print(type(t))
print(type(x))

x[0] = 3
print(x)

# immutable

t = (3, 2, 3)
print(t)
print(id(t))
print(len(t))

t = ("Kiyan", 16)
print(t)

t = 1, 2, 3
print(t)
print(t[0])
print(t[2])

t = t + (12, )
print(t)
t = "Kiyan", 16
print(t.index("Kiyan"))
print(t.index(16))
t = "Kiyan", 16, 16
print(t.count("Kiyan"))
print(t.count(16))
print(t.count(25))

record = "Iran", 2024, 7, 19
print(record)

# unpacking
country, year, month, day = record
print(country)
print(year)

country, *a73g5, day = record
print(country)
print(a73g5)
print(day)

x = 25
y = 12

# swap جابه جا کردن

y, x = x, y
print(x, y)