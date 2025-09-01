str1 = '23*24*+'
list1 = []


for i in str1:
    if i.isnumeric():
        list1.append(int(i))
    else:
        if len(list1) < 2:
            print('Invalid postfix')
            break
        else:
            num1 = list1.pop()
            num2 = list1.pop()

            if i == '*':
                list1.append(num2 * num1)
            elif i == '+':
                list1.append(num2 + num1)
            if i == '-':
                list1.append(num2 - num1)
            if i == '/':
                list1.append(int(num2 / num1))

print(list1)
            




