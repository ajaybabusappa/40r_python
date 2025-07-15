#push
#pop
#is_empty
#peek
#size

stack = []


def push(elem):
    stack.append(elem)

def size():
    return len(stack)

def peek():
    if len(stack) == 0:
        return 'No elements in the stack'
    return stack[-1]

def is_empty():
    return len(stack) == 0


def pop():
    if is_empty():
        return 'Nothing to pop'
    return stack.pop()




#1. push 2. pop 3. size 4. is_empty() 5.peek 
#Anything other than 1 to 5. Exit

while True:
    input_op = input('Choose 1.Push 2.  pop 3. size 4. is_empty() 5.peek')

    if input_op == '1':
        push_input = input('Enter element to push')
        push(push_input)
    elif input_op == '2':
        print(pop())
    elif input_op == '3':
        print(size())
    elif input_op == '4':
        print(is_empty())
    elif input_op == '5':
        print(peek())
    else:
        print('Invalid input selected')
        break



list1 = [1, 2, 3, 4]
del list1[0]
print(list1)