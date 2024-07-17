list_ =[1, 2, 3, 4, 5, 6, 7]
print(list_)
print(type(list_))

list_ = ["kiyan", 3, 13.1, True]
print(list_)

print(len(list_))

print(list_[0])
print(list_[1])

num_list = [1, 2, 3]

print(list_ + num_list)

print(num_list * 3) # num_list + num_list + num_list

num_list.append(10)
print(num_list)

# mutable
num_list[0] = 9
print(num_list)

num_list.extend([11, 10, 1])
print(num_list)

num_list.pop()
print(num_list)

num_list.pop(1)
print(num_list)

popped_item = num_list.pop()
print(popped_item)
print(num_list)

num_list.insert(1, 2)
print(num_list)

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

nested_list =[1, 2, [19, 4], "kiyan", [True, "Mousavi"]]
print(nested_list)

print(nested_list[2][1])