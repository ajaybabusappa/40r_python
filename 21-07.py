#Inheritance
#Polymorphism => Operator overloading 
#Dunder methods or magic methods


#Encapsulation => Hide data or variables
#Abstraction => 


# def sum(a, b):
#     pass


# def sum(a, b, c):
#     pass


# def sum (a, *b):
#     pass


# sum()
# sum(2, 4, 5, 6, 7)


print(2 + 3)

#Dunder methods or magic methods
#Double underscore method

#Dunder method
#Object life cycle -   #__init__(), __del__()
#Arthematic => +, - ... #__add__()
#string => __str__()
#len() => __len__()


#Operator overloading => __add__()



class Student:
    def __init__(self, name, study_class, subjects, marks):
        self.name = name
        self.study_class = study_class
        self.subjects = subjects
        self.marks = marks
        print(self.name, 'Student object created')


    def __del__(self):
        print(self.name, 'and all his records are deleted')


    def __add__(self, other_student):
        return self.marks + other_student.marks
    
    def __sub__(self, other_student):
        return self.marks - other_student.marks

    def __str__(self):
        return str((self.name, self.study_class, self.marks))
      
s1 = Student('Krishna', 9, ['M', 'So', 'Sc'], 77)
s2 = Student('Rama', 9, ['M', 'So', 'Sc'], 84)

print(s1 + s2) # (s1).__add__(s2)
print(s1 - s2)

print(s1)
print(len(s1))




    

