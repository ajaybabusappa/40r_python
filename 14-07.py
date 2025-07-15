#4 main pillars of OOP => Inheritance, poly, abstraction, encapsulation

#Inheritance.
#Calc => add, sub, mul, div, expo
#Adv calc => 
#Super calc => 



class Calc: #Parent class, Super class
    company = 'CASIO'
    registration_id = 'RID12415'

    def __init__(self, id, manf_date):
        self.id = id
        self.manf_date = manf_date
        print('Calc object created')

    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    

class AdvCalc (Calc):#Child class, sub class
    def __init__(self, id, manf_date):
        super().__init__(id, manf_date)
        print('AdvCalc created')
    
    def log (self, a):
        return 5
    
    def add (self, a, b):
        super().add(a, b)
        return a + b + 1
    

adv1 = AdvCalc('32', 'Jan 14')
print(adv1.add(2,5))
print(adv1.company, adv1.registration_id)
print(adv1.id, adv1.manf_date)




#
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n//2 or j == 0 or j == n-1:
            print('*', end= ' ')
        else:
            print(' ', end=' ')
    print()