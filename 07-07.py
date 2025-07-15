# #OOPS
# #Procedural programming disadvatanges 

# #Class and Object
# #Constructor => Method 




# class Human: #Every entity knows something and does something

#     def __init__(self, ip_name, ip_age):
#         self.name = ip_name
#         self.age = ip_age
#         print('Human object is created')


#     def speak(self):
#         print("A Human is speaking")

#     def walk(self):
#         print('A human is waling')


# hum1 = Human('Balayya', 19)
# hum2 = Human('Sivayya', 22)
# hum3 = Human('Kanayya', 35)
# hum4 = Human('Annaya', 42)

# print(hum1.name, hum4.age)










# hum1.speak()

# hum1.name = 'Balayya'
# hum1.age = 19

# hum2.name = 'Mohan babu'
# hum2.age = 80

# print(hum1.name, hum1.age)
# # print(hum3.name, hum4.age)




#color, vehicle_num, engine_num, model_num
#3 methods - drive, start and horn, stop


class Car:

    company_name = 'Tata'
    company_reg_num = 'GSTIN123131'
    count = 0

    def __init__(self, input_color, input_veh_num, input_eng_num, input_model_num):
        self.color = input_color
        self.veh_num = input_veh_num
        self.eng_num = input_eng_num
        self.model_num = input_model_num
        Car.count += 1
        print('One car object created')

    def describe(s1):
        print(s1.color, s1.veh_num, Car.company_name)

    def drive(self):
        print('Car in driving mode')

    def change_color(self, input_color):
        self.color = input_color
        print('Color changed')

    def get_color(self):
        return self.color 
            


car1 = Car('red', 123, 345, 456)
car2 = Car('blue', 124, 345, 456)
print(Car.count)
car3 = Car('black', 125, 345, 456)
car4 = Car('green', 126, 345, 456)

# car2.drive()
car1.describe()
print(Car.count)
print(car1.count, car2.count)

# car2.change_color('black')
# car2.color = 'black'
# print(car2.get_color())



#Variables or attributes or datafields
#Methods


#Variables => Instance, class/static variables
#Instance variable's value depends on a particular instance
#Static/class variable's value is fixed at class level

#Access => 

#print(Car.color)


# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
