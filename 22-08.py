#Lambda functions: 



def add(a, b):
    return a + b


example_function = lambda a, b: a + b
# print(example_function(2))
print(example_function(5, 10))
example_function = 44
# print(example_function(4, 12))


function1 = lambda : 'Lunch ayindha'
# print(function1('?'))


#Higher order functions - map, filter and reduce
#map (function, iterable)


print(list(map(lambda x: x ** 6, [1, 2, 5, 10, 22, -4])))

#Balayya
print(list(map(lambda x: x ** 2, [11, 2, 5, 111, 211, -4])))



print(list(filter(lambda x: x % 3 == 0 or x % 7 == 0, [11, 2, 5, 111, 211, -4])))