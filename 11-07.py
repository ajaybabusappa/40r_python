# #Methods => instance, class and static

# #Decorators


# def example_decorator(func):
#     def wrapper():
#         print('Check A4 sheets and Ink')
#         func()
#         print('Task completed. Thank you')
#     return wrapper


# @example_decorator
# def printer():
#     print('I am printing')

# printer()



# @example_decorator
# def scanner():
#     print('Scan')

# scanner()



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

    
    @classmethod
    def reset_company_details(cls):
        Car.company_name = 'Birla'
        Car.company_reg_num = 'GSTIN123122'
        Car.count = 0


    @staticmethod
    def describe_company():
        print('Jai Balayya....Gundelllo Gollaya')

    def describe(s1):
        print(s1.color, s1.veh_num, Car.company_name)

    def drive(self):
        print(self.veh_num, 'Car in driving mode')

    def change_color(self, input_color):
        self.color = input_color
        print('Color changed')

    def get_color(self):
        return self.color 



car1 = Car('red', 123, 345, 456)
car2 = Car('blue', 124, 345, 456)
car3 = Car('black', 125, 345, 456)
car4 = Car('green', 126, 345, 456)


car1.get_color()

Car.reset_company_details()
car1.reset_company_details()

# Car.describe_company()
car1.describe_company()
