# #Unordered unique elements
# #Inset u can only take immutable data
# set1 = {2, 1, 3, 5, 'str1', 'str2'}
# #set2 = Set()
# print(type(set1))
# print(set1)


# #Inbuilt functions

# set1.add(8)
# set1.add(8)
# print(set1)

# # set1.remove(2)
# # set1.remove(2)
# set1.discard(2)
# print(set1)
# set1.discard(2)
# print(set1)


# #clear 
# # set1.clear()
# print(set1)

# set2 = set1.copy()
# print(set2)
# print(set1)


#union, intersection, difference, symmetric_difference
#issubset, issuperset
#isdisjoint


set1 = {1, 2, 3}
set2 = {1, 2, 5, 6}

# print(set1.union(set2)) #set1 | set2
# print(set2.union(set1))

#Intersection - set1 & set2

#Difference
# print(set1.difference(set2))
# print(set2.difference(set1))


# print(set1.symmetric_difference(set2))
# print(set2.symmetric_difference(set1))

# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))



# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)
# print(set2 - set1)
# print(set1 ^ set2)
# print(set2 ^ set1)

#Pop
set1 = {1, 2, 3, 4, 's1', 's2'}
print(set1)
# print(set1.pop())
# print(set1.pop())
# print(set1.pop())
# print(set1.pop())
# print(set1.pop())
# print(set1.pop())
# print(set1.pop())



# list1 = [1, 2,2,4, 5, 7,8]
# list1 = list(set(list1))
# print(list1)



print(len(set1))

set_len = len(set1) #6

# while set_len > 0:
#     print(set1.pop())
#     set_len -= 1


# while len(set1) > 0:
#     print(set1.pop()) 


# while set1 != set():
#     print(set1.pop())


while set1:
    print(set1.pop())


str1 = 'the sun rises in the east and sets in the west'
print(list(set(str1.split())))


data = [[1, 2], [2, 3], [4, 1]]
#1, 2, 3, 4

set1 = Set()
for i in data:
    for j in i:
        set1.add(j)

print(len(set1))




