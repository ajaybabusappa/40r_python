#Inheritance
#Polymorphism => 
#Abstraction => Hiding something

#Abstact classes 
#You cannot create an object for an abstract class

from abc import ABC, abstractmethod

class PaymentProcess(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass

    def print_details(self):
        print('Here are the details of this payment process')


class UPI(PaymentProcess):
    
    def pay(self, amount):

        print(amount, 'money has be payed to user using UPI')


class DebitCard(PaymentProcess):
    def pay(self, amount):
        print('Debited using debit card')


class NetBanking(PaymentProcess):
    def pay(self, amount):

        print('netbanking used')

upi1 = UPI()




#Patterns

# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5



n = 7

for i in range(n):
    num1 = 1
    for j in range(n):
        if i >= j:
            print(num1, end= ' ')
            num1 += 1
        else:
            print(' ',end= ' ')
    print()



num1 , num2 = 0, 1
#0, 1, 1, 2, 3, 5, 8, 13


for i in range(n):
    print(num1)
    third_num = num1 + num2
    num1 = num2
    num2 = third_num



for i in range(n):
    print(num1)
    num1, num2 = num2, num1 + num2
    
