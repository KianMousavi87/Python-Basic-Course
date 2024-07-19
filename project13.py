def find_common(list1, list2):
    list_ = []
    for item in list1:
        if item in list2:
            if item not in list_:
                list_.append(item)
    return list_

print(find_common([1, 3, 7,], [7, 2, 12]))
print(find_common([1, 1, 12, 7], [1, 5, 2]))
print(find_common([1, 3, 2, 12], [3, 2, 2, 23]))

def search(list_, n):
    for index, element in enumerate(list_):
        if n == element:
            return index
    return -1
    
print(search([1, 2, 3], 4))
print(search([5, 2, 12], 5))
print(search([2, 5, 12], 5))
print(search([2, 5, 5], 5))