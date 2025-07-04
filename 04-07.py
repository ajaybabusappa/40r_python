# #Dictionary comprehension

# # dict1 = {}

# # for i in range(1, 10):
# #     dict1[i] = i * i

# # print(dict1)

# # dict2 = {i: i * i for i in range(1, 10)}
# # print(dict2)


# dict2 = {i: i * 2 for i in range(1, 10)}
# print(dict2)

# dict2 = {i: i * 2 for i in range(1, 10) if i % 2 == 0}
# print(dict2)

# l1 = ['k1', 'k2']
# l2 = ['v1']

# dict3 = {l1[i] : l2[i] for i in range(min(len(l1), len(l2)))}
# print(dict3)

# l1 = ['k1', 'k2']
# l2 = ['v1', 'v2', 'v3']

# dict3 = {l1[i] : (l2[i] if i < len(l2) else '') for i in range(len(l1))}
# print(dict3)



# dict1 = {1: '1', 2: '2', 3: '3', 4: '4'}

# dict2 = {value: key for key, value in dict1.items()}
# print(dict2)


#OOPS

# def add (a, b):
#     return a + b


# def drive_car():
#     print('You are driving a car')

# def sub(a, b):
#     return a - b

#camelcase schoolDirectory
#pascalcase SchoolDirectory
#snakecase school_directory



# class Calculator: 
#     def add(self):
#         print("Add function called")



# calc1 = Calculator()
# calc2 = Calculator()

# calc1.add()
# calc2.add()



mat1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 9, 1, 0],
    [5, 6, 7, 8],
]

# for i in mat1:
#     for j in i:
#         print(j, end = ' ')
#     print()


sum = 0
for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        if i == j:
            sum += mat1[i][j]
            print(mat1[i][j], end= ' ')
        else:
            print('*', end=' ')
    print()



sum = 0
n = len(mat1)
for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        if i == j or i + j == n-1:
            sum += mat1[i][j]
            print(mat1[i][j], end= ' ')
        else:
            print('*', end=' ')
    print()






