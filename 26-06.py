#Type casting

# num1 = input('Enter num1') #'5'
# num2 = input('Enter num2')

# num1 = int(num1) #5

# print(num1 - num2)

num1  = 5.6
num1 = int(num1)
print(num1)
num1 = float(num1)
print(num1)



#Numeric - int, float, complex, bool
num1 = 23
num1 = complex(num1)
print(num1)
#k + mj
#23 + 0j


# cmp1 = 2 + 3j
# cmp1 = int(cmp1)


print(bool(-5))
print(bool(5))
print(bool(0))

#Truthy values and falsy values
#Falsy - 0, [], '', (), {}, None, 0+0j

# if is_he_alive:
#     print('Super')


age = -5

if age:
    print('Eligible to vote')



print(float(0))



#int, float, cmp, bool
#string, list, tuple, range
#set, dictionary
#None


num1 = 5
# num1 = tuple(num1)
# print(num1)

print(range(num1)) #range(0, 5)


rng1 = range(11, 25)
print(list(rng1))


#int to string #53 => '53'
#'53' to int 53
#'53.4' to int 

#77.3


int1 = 2
flt2 = 2.2
print(int1 + flt2) #4.2



#Inbuilt functions


#Find the key with max value

dict1 = {'k1': 23, 'k2': 45, 'k3': 22, 'k4': -3}

list1 = [23, 45, 22, -3]
max = float('-inf') #float('inf')

for i in list1:
    if i > max:
        max = i
print(max)


dict1 = {'k1': 23, 'k2': 45, 'k3': 22, 'k4': -3}
max = float('-inf')
max_key = ''
for key, value in dict1.items(): #k2, 45
    if value > max:
        max = value #23 #45
        max_key = key

print(max, max_key) #45


dict1 = {'k1': 21, 'k2': 45, 'k3': 22, 'k5': -3}
dict2 = {'k1': 23, 'k5': 45, 'k7': 22, 'k0': -3}

#{'k1': 44, 'k5': 42}


dict3 = {}

for key, value in dict1.items():
    dict3[key] = value

#dict3 is same as dictionary 1

for key, value in dict2.items():
    if key in dict1: #dict3
        dict3[key] += value
    else:
        dict3[key] = value

print(dict3)




#['green', 'blue', 'GREEN', 'Red', 'RED']
#sock
#Monday => Tuesday
