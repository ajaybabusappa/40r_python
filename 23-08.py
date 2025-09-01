list1 = [234, 756, 819, 345]

def check_order (num1): #6789
    prev_rem = 9.1
    while num1 > 0:
        rem = num1 % 10 #9 #8 #7 #6
        if rem >= prev_rem:
            return False
        num1 = num1 // 10 #678 #67 #6 #0
        prev_rem = rem #9 #8 #7 #6

    return True


for i in list1:
    print(check_order(i))





#Find substrings
#abbdefg
#a
#ab
#abb
#abbd
#abbde
#b
#bb
#bbd
#bbde
#b
#bd
#bde

def check_palindrome(str1):
    return str1 == str1[ : : -1]



str1 = 'abdbabg'
#pal_list = []
max_len = 0
max_str = ''
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        substr = str1[i: j]
        if check_palindrome(substr):
            if len(substr) > max_len:
                max_len = len(substr)
                max_str = substr

            # pal_list.append(substr)


# pal_list.sort(key = len)
# print(pal_list[-1])

print(max_str)





list1 = [22, 33, 44, 55, 66, 77]


def check_ascending(input_list):

    for i in range(len(input_list) - 1):
        if input_list[i] > input_list[i + 1]:
            return False
        
    return True


def check_descending(input_list):

    for i in range(len(input_list) - 1):
        if input_list[i] < input_list[i + 1]:
            return False
        
    return True


def any_sort (input_list):
    return check_ascending(input_list) or check_descending(input_list)



list1 = [22, 33, 44, 5, 66, 77]
list1.reverse()
# print(any_sort(list1))






