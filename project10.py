# [0, 1, 2, 3, 4, 5]

list_ = []
for i in range(6):
    list_.append(i)

print(list_)
# List comprehension
list_ = [i for i in range(6)] # {i | i <=6}
print(list_)
# List comprehension
# " hello"
list_ = [c for c in "hello"]
print(list_)
# Ring
list_ = []
for i in range(10):
    list_.append(i ** 2)
print(list_)
# List comprehension
list_ = [i ** 2 for i in range(10)]
print(list_)

list_ = []
for i in range(10):
    if i % 2 == 0:
        list_.append(i)
print(list_)
# nasted list
matrix = []
for i in range(5):
    row = []
    for j in range(1, 6):
        row.append(5 * i + j)
    matrix.append(row)
print(matrix)

matrix = [[5 * i + j for j in range(1,6)] for i in range(5)]
print(matrix)

l1 = ['a', 'b']
l2 = ['x', 'y']
# ['ax', 'ay', 'bx', 'by']

# 'a' + 'x' ===> 'ax'
  # List comprehension
list_ = [c1 + c2 for c1 in l1 for c2 in l2]
print(list_)