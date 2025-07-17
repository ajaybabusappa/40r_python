#Types of Inheritance - Single, Multilevel, multiple, H and H
#MRO 


# class A (C, B):
#     pass


#Polymorphism => Method overiding, M.Overloading, O.Overloading


print(2 + 3)
print((2).__add__(3))
print('2' + '3')

print(2 > 3)




class BankAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance
        print('Account created succesfully')

    
    def __add__(self, other): #Adds balance of both objects
        #print('Adding 2 bank account')
        return self.balance + other.balance
    
    def __gt__(self, other1):
        return self.balance > other1.balance
    

# ba1 = BankAccount('123', -35)
# ba2 = BankAccount('234', -32)


# print(ba1 + ba2) #(ba1).__add__(ba2)
# print(ba1 > ba2)




#Encapsulation => 

#Hide the data 



class BankAccount:
    def __init__(self, acc_num, balance):
        self._acc_num = acc_num
        self.__balance = balance
        print('Account created succesfully')

    def __add__(self, other): #Adds balance of both objects
        #print('Adding 2 bank account')
        return self.balance + other.balance
    
    def __gt__(self, other1):
        return self.balance > other1.balance
    
    def get_balance(self):
        return self.__balance
    

    def set_balance(self, new_balance):
        self.__balance = new_balance

ba1 = BankAccount('234', 7999)

print(ba1._acc_num)
print(ba1.__balance)

ba1.balance = -1000

# ba1.balance = 10000000
# print(ba1.get_balance())
# print(ba1.balance)


#Access specifiers
#Public, Protected, Private

#_age
