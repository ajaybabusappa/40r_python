list1 = [222, 11, -32, 45, -72, -322]
#[11, 222, -32, 45, -72, -322]
#[11, -32, 222, 45, -72, -322]
#[11, -32, 45, 222, -72, -322]
#[11, -32, 45, -72, 222, -322]
#[11, -32, 45, -72, -322, 222]


# a = 10
# b = 20
# a, b = b, a



for j in range(0, len(list1)-1):
    flag = True
    for i in range(len(list1) - 1 - j): #i = 5
        if len(list1[i]) > len(list1[i+1]):
            flag = False
            list1[i], list1[i+1] = list1[i+1], list1[i]
        
    if flag == True:
        break

    print(list1)


#1st iteration -> j = 0 => 0 neglect
#2nd iteration -> j = 1 => 1 neglect
#3rd iteration -> j = 2 => 2 neglect



[2, 3, 4, 6, 5]

#Nowhere in the list, ith element is 
# greater than i + 1 element


['str1', 'sttr2', 'dadsafsa', 'fasfsfsafsa']



[[1, 2, 3], [-5, 6, 22], [-2], [1, 22, 23], [32]]
[[-5, 6, 22], [-2], [1, 2, 3], [1, 22, 23], [32]]
