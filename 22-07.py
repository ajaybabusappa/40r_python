# #
# list1 = [1,3,9,5,2]
# list2 = [2,4,3,1,7,5,15]

# print(set(list1).issubset(set(list2)))
# print(set(list2).issubset(set(list2)))


# # flag = True

# # for i in list1:
# #     if i not in list2:
# #         flag = False
# #         print('Not subset')
# #         break

# # if flag == True:
# #     print('Subset')



# # def is_subset(l1, l2):

# #     for i in l1:
# #         if i not in l2:
# #             return False
        
# #     return True


# # print(is_subset(list1, list2))


# list2 = [2,4,3,1,7,5,15] 

# #Method 1
# #list2 = list2[::-1]
# #print(list2)


# #Method 2 =. O(n), O(n)
# new_list = []
# for i in list2:
#     new_list.insert(0, i)

# list2 = new_list
# print(list2)




list2 = [2,4,3,1,7,5,15] 

low, high = 0, len(list2) -1

while low < high:
    list2[low], list2[high] = list2[high], list2[low]
    low += 1
    high -= 1

print(list2)

#O(1)
#O(n/2) => O(n)




#USER_ID USER_NAME PH_NUM COURSE_ID COURSE_NAME DEPARTMENT
# 1      Hari      915141 204       DBMS        CSE
# 1      Hari      915141 205       DSD         ECE
# 3      Janaki    915141 206                 MECH
# 2      BALA      916141 204       DBMS        CSE 

#Insert, update and delete anamoly


#user_id 
#user_id, user_name 
#user_id, user_name, user_ph
#ph_num

#user_name


#USERS_TABLE 
#1 HARI 915141
#2 BALA 916141


#COURSE_TABLE
#204 DBMS CSE
#205 DSD  ECE
#206 ED   MECH


#ASSOCIATION_TABLE
#1 204
#1 205
#1 206
#2 204
#


#STU_ID   STU_NAME  STU_PH_NUM COURSE_ID COURSE_NAME COURSE_CRED INST_ID INST_NAME INST_DEPT  
#1        Surya     8819       101, 102,  DSD, ED,SE  3, 3,4     1, 2, 3  'A',B, C  ECE, CSE, MECH
#                               103


#1NF - ATOMICITY

#STU_ID   STU_NAME  STU_PH_NUM COURSE_ID COURSE_NAME COURSE_CRED INST_ID INST_NAME INST_DEPT  
#1        Surya     8819       101       DSD         3           1       'A'  ECE
#1        Surya     8819       102       ED          3           2       'B'  CSE
#1        Surya     8819       103       SE          4           3       'C'  MECH 



#2NF => 2nd normal form
#It should be in 1NF first
#Partial dependencies => No

#(stu_id, course_id)

#Student_table

#STU_ID STU_NAME STU_PH_NUM 
#1      Surya    8819


#Couse table
#COURSE_ID COURSE_NAME COURSE_CRED INST_ID INST_NAME INST_DEPT
#101       DSD         3           1       'A'  ECE
#102       ED          3           2       'B'  CSE
#103       SE          4           3       'C'  MECH 


#stu_course_table
#stu_id course_id
#1      101
#1      102
#1      103



# 3NF
#It should be in 2NF
#There should be no transitive dependency



#COURSE_ID COURSE_NAME COURSE_CRED INST_ID
#101       DSD         3           1       
#102       ED          3           2       
#103       SE          4           3       


#INST_ID INST_NAME INST_DEPT
#1       'A'  ECE
#2       'B'  CSE
#3       'C'  MECH 





#STU_ID   STU_NAME  STU_PH_NUM COURSE_ID COURSE_NAME COURSE_CRED INST_ID INST_NAME INST_DEPT  
#1        Surya     8819       101       DSD         3           1       'A'  ECE
#1        Surya     8819       102       ED          3           2       'B'  CSE
#1        Surya     8819       103       SE          4           3       'C'  MECH 
#2        Karthi    8820       101       DSD         3           4       'D'  ECE

#(student_id, course_id)

#COURSE_ID COURSE_NAME COURSE_CRED INST_ID INST_NAME INST_DEPT
#101       DSD         3           1       'A'  ECE
#102       ED          3           2       'B'  CSE
#103       SE          4           3       'C'  MECH 
#101       DSD         3           4        'D'  ECE

#COURSE_TABLE
#101
#102
#103

#INST_TABLE


#ASSOCIATION COURSE INST
#C_ID  I_ID
#404   101   #P1

#STU_ID COURSE_INT_ASSOCIATION_ID
#1      P1
#2      P1







#users_table
#user_id  user_name user_ph dept_id
#1        'Ramesh'  8121    101 
#2        'Suresh'  8122    102
#3        'Mahesh'  8123    NULL


#department_table
#dept_id  dept_name dept_loc
#101        CSE       Hyd
#102        ECE       Hyd
#105        IT        Hyd
  

#Inner join 