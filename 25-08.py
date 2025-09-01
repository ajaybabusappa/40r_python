#Stack operations
#Push
#pop 
#is_empty()
#peek


list1 = []


def push(input_list, elem):
    input_list.append(elem)
    return

def stack_pop(input_list):
    if len(input_list) < 1:
        return 
    elem = input_list.pop()
    return elem

def is_empty(input_list):
    return len(input_list) == 0


def peek(input_list):
    if len(input_list) < 1:
        return 
    return input_list[-1]




# push(list1, 5)
# print(list1)

# print(peek(list1))
# print(is_empty(list1))
# push(list1, 6)
# print(list1)

# res = stack_pop(list1)
# print(res)
# print(list1)


# res = stack_pop(list1)
# print(res)
# print(list1)





str1 = 'kudumulu'

for i in str1:
    push(list1, i)

new_str = ''

while not is_empty(list1):
    elem = stack_pop(list1)
    new_str += elem

print(new_str)



