def add(a, b):
    return a + b

print(type(add))
print(id(add))
print(add(2, 3))

result = add(2, 3) # result = name
print(result)

def say_hello():
    print("Hello kiyan")

say_hello()
result = say_hello()
print(result)


def greeting(name):
    return f"Hello {name}"

result = greeting("kiyan")
print(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(1)) # Prime number
print(is_prime(2))
print(is_prime(5))
print(is_prime(49))

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(3))
print(fact(5))

def compute_add_sub(a, b):
    return a + b, a - b

print(compute_add_sub(2, 3))

def rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter
print(rectangle(2, 3))