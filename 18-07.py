# list1 = [1, 2, 3, 31, -2, 5]


# def rotate_list(list1, k):
#     if len(list1) == 0:
#         return list1
    
#     for i in range(k % len(list1)):
#         last_elem = list1.pop()
#         list1.insert(0, last_elem)
#     return list1

# k = int(input('Enter number of rotations'))

# list1 = rotate_list(list1, k)
# print(list1)


k = 1000
list1 = [1, 2, 3, 31, -2, 5]

list1 = list1[-(k % len(list1)): ] + list1[0 : -(k % len(list1))]
print(list1)




n = 4

matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for i in range(n):
    for j in range(n):
        if i > j:
            matrix1[i][j], matrix1[j][i] = matrix1[j][i], matrix1[i][j]


print(matrix1)


