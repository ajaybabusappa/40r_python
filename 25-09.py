#Pandas 
import pandas as pd

# s1 = pd.Series([10, 20, 30], index = ['a', 'b', 'a'])
# print(s1['a'])


# data = {

#     'name': ['Mahesh', 'Ramesh', 'Suresh'],
#     'age': [25, 26, 27],
#     'gender': ['M', 'M', 'M']
# }

# df = pd.DataFrame(data)
# print(df)
# df.to_csv('student_details', index= False)

# print(df['name'])
# print(df['age'].mean())


df = pd.read_csv('data.csv')
print(df.head(3))
print('-----------')
print(df.tail(3))

print(df.shape)
print(df.info())

print('------------')
print(df.describe())
print(df.dtypes)
print(df.columns)

print(df.index)

# for i in df.index:
#     print(i)


print(df[['Name', 'Survived']])

print(df.loc[[2, 3, 4], ['Age', 'Name']])
print(df.iloc[[2, 3, 4], [0, 1]])

print(df[df['Age'] > 30][df['Survived'] == 1][['Age', 'Survived', 'Name']])

print('---------------')
print(df.groupby("Sex")["Age"].mean())