list_ = [i for i in range(20)]
print(list_)
print(list_[0], list_[3])
print(list_[3:8:2]) #[start, stop]
row1 = [1, 2, 3, 4, 5]
row2 = [6, 7, 8, 9, 10]
row3 = [11, 12, 13, 14, 15]
row4 = [16, 17, 18, 19, 20]
matrix = [row1, row2, row3, row4]
print(matrix[::2][0][2::2],matrix[::2][1][2::2])
#list_[0] = 3 false
#name[0] = "r" false
name = "kiyan" # name = miutebel
print(name[::-1]) # Reverse