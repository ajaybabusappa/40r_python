# # #
# # num1 = int(input('Enter a number'))
# # #3456
# # temp = num1
# # count = 0

# # while temp > 0:
# #     digit = temp % 10
# #     count += 1
# #     temp = temp // 10
    
# # print(count)

# # #Armstrong number
# # #153
# # num1 = int(input('Enter a number')) #1234
# # temp = num1
# # sum = 0

# # while temp > 0: #temp = 153 #15 #1 #0
# #     digit = temp % 10 #3 #5 #1
# #     sum += digit ** count #27 #152 #153
# #     temp = temp // 10# 15 #1 #0
    
# # if sum == num1:
# #     print('Armstrong')
# # else:
# #     print('Armsweak')
    
    
    
# # #Sum of first n 
# # n = int(input("Enter number"))

# # fact = 0

# # for i in range(1, n + 1):
# #     fact *= i

# # print(fact)
    
# # 7 => 1 + 2 + 3 ... + 7
# #7 => 1 * 2 * 3 * 4 * 4.. 7

# #
# dict1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v1',
#     'k5': 'v3'
# }
# #
# dict2 = {}

# for key, value in dict1.items():
#     if value not in dict2:
#         dict2[value] = key
        
# # print(dict2)
# # {'v1': ['k1', 'k4'], 'v2': ['k2'], 'v3': ['k3', 'k5']}
# dict1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v1',
#     'k5': 'v3'
# }
# dict2 = {}

# for key in dict1: #k1
#     if dict1[key] not in dict2: #v1
#         dict2[dict1[key]] = [key]
#     else:
#         dict2[dict1[key]].append(key)


# print(dict2)     


# dict1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v1',
#     'k5': 'v3'
# }
# dict2 = {}

# for key, value in dict1.items():
#     if value not in dict2:
#         dict2[value] = [key]
#     else:
#         dict2[value].append(key)

# print(dict2)
        

#Max value and key in a dictionary
#Anagram

#LISTEN, SILENT 
#BELOW, ELBOW => BELOW
#AJAY, JAYA => AAJY, AAJY

#SORTING

str1 = 'BELOW'
str2 = 'ELBOW'

if sorted(str1) == sorted(str2):
    print('Anagram')
else:
    print('Not anagrams')
    
    
#Method 2

str1 = 'anagram'
str2 = 'nagaram'

dcit1 = {}
for i in str1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
        
dcit2 = {}
for i in str2:
    if i not in dict2:
        dict2[i] = 1
    else:
        dict2[i] += 1
        
if dict1 == dict2:
    print
        
        



    
    
##BELOW
{
    'B': 1
    'E': 1,
    'L': 1,
    'O': 1,
    'W': 1
}
#ELBOW

{
    'B': -2
    'E': 0,
    'L': 0,
    'O': 0,
    'W': 0
}
