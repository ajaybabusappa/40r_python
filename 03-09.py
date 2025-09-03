#Exception handling
#Error

# a = int(input('Enter a'))
# b = int(input('Enter a'))


# try: 
#     print(a / b)
#     print(int('abc'))
# except Exception as e:
#     print(e)
#     print('Division failed because of somereason')
# else:
#     print('Division completed succesfully')
# finally:
#     print('Finally check')



# print('These are important tasks')


# print(int('abc'))

# print(2 + '3')


# num1 = 2
# num1.upper()


import copy
list1 = [1, 2]
copy.deepcopy(list1)


list1.copy()


# print([0] * (10 ** 10))


# while True:
#     print('Hi')




a = 10
b = 0
try: 
    # print(int('abc'))
    print(a / b)

except (ValueError, ZeroDivisionError):
    print('Your inputs are wrong')
except Exception as e:
    print(e)
    print('Division failed because of somereason')
except ZeroDivisionError:
    print('Your trying to divide 2 numbers in which denominator is zero')

else:
    print('Division completed succesfully')
finally:
    print('Finally check')


class WrongPinException (Exception):
    pass


def chech_balance(pin):

    # raise ValueError
    try:
        if pin != 'original pin':
            raise WrongPinException('ERROR 234')
    except WrongPinException as wpe:
        print(wpe)
        print('You entered wrong pin')

chech_balance(722)
