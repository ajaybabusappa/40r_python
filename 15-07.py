# #Inheritnace 

# class A: #Base
#     def add (self, a, b):
#         return a + b


# class B (A): #Derived class
#     def add (self, a, b):
#         return a + b + 1



# #Method overriding 

# a1 = A()
# a1.add(4, 5)

# b1 = B()
# b1.add(4, 5)



#Multi level Inheritance

class Teacher:
    def teach_class (self):
        print('Teacher is teaching') 

class ClassTeacher (Teacher):
    def teach_class(self):
        print('Class teacher is teaching')

class Admin(ClassTeacher):
    pass


t1 = Teacher()
t1.teach_class()

ct1 = ClassTeacher()
ct1.teach_class()

# adm1 = Admin()
# adm1.teach_class()

# print(Admin.mro())



#Multiple Inheritance
class Lion:
    def roar(self):
        print('Balayya is roaring')

    def hunt(self):
        print('Balayya is hunting')

class Tiger:
    def hunt(self):
        print('Tiger is hunting')

class Liger (Tiger, Lion):
    pass


l1 = Liger()
l1.hunt()
# l1.roar()
#MRO => Method resolution order

print(Liger.mro())



#Hieriarchial intheritance

class Animal:
    pass


class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Horse(Animal):
    pass



#Hybrid




#Polymorphism => Many, forms
#Method overriding, M overloading, Operator overloading

#Method overloading





class Tiger:
    def hunt(self):
        print('Tiger is hunting')

    def hunt(self, prey):
        print('Tiger is huting the prey')

    
    



#Operator overloading
# print(2 + 3)
# print((2).__add__(3))
# print(2 * 3)
# print('2' + '3')



# t1 = Tiger()
# t2 = Tiger()

# print(t1 + t2)


n = 7

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or (j == n-1 and i >= n//2) or (i == n//2 and j >= n//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()









