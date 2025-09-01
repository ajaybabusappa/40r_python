#Iterators and Generators

#Iterable => 

# list1 = [10, 20, 23, 45, 67, 81]

# # for i in list1:
# #     print(i)

# # itr1 = iter(list1)
# # print(itr1)
# # print(next(itr1))
# # print(next(itr1))
# # print(next(itr1))
# # print(next(itr1))
# # print(next(itr1))
# # print(next(itr1))
# # print(next(itr1))



# #Custom Iterators

# class EvenNumbers:
#     def __init__(self, start_num):
#         self.current_val = start_num

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         #current_val
#         if self.current_val < 0:
#             raise StopIteration

#         temp = self.current_val
#         self.current_val -= 2
#         return temp


# en1 = EvenNumbers(10)
# print(next(en1))
# print(next(en1))
# print(next(en1))
# print(next(en1))
# print(next(en1))
# print(next(en1))




# class RangeIterator:
#     def __init__(self, start_num, end_num):
#         self.current_val = start_num
#         self.end_val = end_num

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         #current_val
#         if self.current_val >= self.end_val:
#             raise StopIteration

#         temp = self.current_val
#         self.current_val += 1
#         return temp


# ri1 = RangeIterator(10, 15)
# print(next(ri1))
# print(next(ri1))
# print(next(ri1))
# print(next(ri1))
# print(next(ri1))
# # print(next(ri1))



# list1 = [10, 20, 23, 45, 67, 81]

# class CustomListIterator:
#     def __init__(self, list1):
#         self.current_ind = 0
#         self.data = list1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         #current_val
#         if self.current_ind >= len(self.data):
#             raise StopIteration

#         temp = self.data[self.current_ind]
#         self.current_ind += 1
#         return temp
    

# cli1 = CustomListIterator([10, 11, 23, -32])
# print(next(cli1))
# print(next(cli1))
# print(next(cli1))




#

def example_gen(n):
    while n > 0:
        print('Output from while')
        yield n
        n -= 2


gen1 = example_gen(8)
print(next(gen1))
print('Output from main')
print(next(gen1))
print('Output from main')
print(next(gen1))




def gen_fib():

    
    num1, num2 = 0, 1
    while True:
       yield num1
       num1, num2 = num2, num1 + num2


gn2 = gen_fib()
print(next(gn2))
print(next(gn2))
print(next(gn2))
print(next(gn2))
print(next(gn2))



def generate_nums():
    count = 0
    while True:
        yield 25
        if count == 5:
            return 50
        count += 1

gn3 = generate_nums()
print('-------------------------')
print(next(gn3))
print(next(gn3))
print(next(gn3))
# print(next(gn3))
# print(next(gn3))
# print(next(gn3))
# print(next(gn3))
# print(next(gn3))



list1 = [i * i for i in range(1, 10)]
print(list1)


gn1 = (i * i for i in range(1, 10))
print(next(gn1))



#2 -> 5 -> 6 -> -9 -> -2
#2 <- 5 <- 6 <- -9 <- -2
#-2 -> -9 -> 6 -> 5 -> 2


# prev = None
# temp = head


# while temp:
#     next_node = temp.next
#     temp.next = prev
#     prev = temp
#     temp = next_node

