# #Recursion - 


# # def printer(n):
# #     if n <= 0:
# #         return 
# #     print(n)
# #     printer(n-1)
# #     print(n)
# #     print(n)


# # printer(7)



# #Factorial of a number
# #5! => 5 * 4 * .... * 1

# #fact(5) = 5 * fact(4) => 4 * fact(3) => 
# #sum(5) = 5 + sum(4)


# def fact(n):
#     if n < 0:
#         return 'Factorial does not exist'
#     if n == 0:
#         return 1
#     if n == 3:
#         return 6
#     return n * fact(n-1)


# print(fact(5))

# #'string' => 'gnirts'
# #reverse('happy') => 'y' + reverse('happ')
# #reverse(gene) => 'e' + reverse('gen') 


# str1  = 'happy'

# def reverse(str1):
#     if len(str1) <= 1:
#         return str1

#     return str1[-1] + reverse(str1[ 0: -1])


# print(reverse(str1))




# #a, b => a * b

# #mul(a, b) => a + mul(a, b-1) => a + a (b-1) => a (b) => ab
#  #mul(5, 7) => 5 + mul(5, 6)


# def mul(a, b):
#     if b == 0:
#         return 0
#     # if b == 1:
#     #     return a

#     return a + mul(a, b-1)


# #a, b 
# #pow(a,b) = a * pow(a, b-1)

# #

# #palindrome('str1') => (str1[0] == str1[-1]) and palindrom(str1[1:-1])



# def power (a, b):

#     if b == 0:
#         return 1
#     return a * power(a, b-1)



# def check_palindrome (str1):
#     if len(str1) <= 1:
#         return True

#     return (str1[0] == str1[-1] )and check_palindrome (str1[1:-1])


# #MADAMIMADAM
# #MADAMINADAM



# #fib(n) = fib(n-1) + fib(n-2)



# def fib(n):
#     # if n == 0:
#     #     return 0
#     # if n == 1:
#     #     return 1
#     if n < 0:
#         return 'Negative numbers not allowed'

#     if n <= 1:
#         return n

#     return fib(n-1) + fib(n-2)


# print(fib(8))



# #23456
# #65432

# #Sum of digits using recursion
# #rev(23456) => 6 * 10 +  rev(2345)



# #sum(23456) => 6 + sum(2345)


# sum = 0
# num1 = 2345
# temp = num1 #2345
# while temp > 0: #234 #23 #2
#     digit = temp % 10 #5 #4 #3 #2
#     print(digit)
#     sum += digit
#     temp = temp // 10 #234 #23 #2 #


# print(sum)




# #sum(23456) => 6 + sum(2345)


# def sum(temp):

#     if temp <= 0:
#         return 0

#     return temp % 10 + sum(temp // 10)





#reverse (23456) => 65432


sum = 0 #6 #65 #654 #6543 #65432
def reverse(temp):
    if temp == 0:
        return
    global sum #6 #65
    sum = sum * 10 + temp % 10 #6 #65 #654
    reverse(temp // 10) # 2345 #234 #23

print(sum)
reverse(23456)
print(sum)