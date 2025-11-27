import pandas as pd

data = {
    'Name' : ['John', 'Anna', 'Peter', 'Alex', 'Max'],
    'Age' : ['27', '45', None, '56', '21'],
    'City' : ['New York', None, 'Florida', 'Las Vegas', 'Moscow']
}

df = pd.DataFrame(data)
df.fillna(0, inplace=True)
print(df, end='\n\n')

'''
Заменяет пустые данные на 0

    Name Age       City
0   John  27   New York
1   Anna  45          0
2  Peter   0    Florida
3   Alex  56  Las Vegas
4    Max  21     Moscow
'''

df.dropna(inplace=True)
print(df)

'''
Пропускает строку в которой есть пустые значения

   Name Age       City
0  John  27   New York
3  Alex  56  Las Vegas
4   Max  21     Moscow
'''

df.drop_duplicates(inplace=True)
print(df)

'''
    Name   Age       City
0   John    27   New York
1   Anna    45       None
2  Peter  None    Florida
3   Alex    56  Las Vegas
4    Max    21     Moscow
'''

df['Age'] = df['Age'].astype(int)
print(df)

'''
Заменяет значения возраста со строк на числа

    Name  Age       City
0   John   27   New York
1   Anna   45          0
2  Peter    0    Florida
3   Alex   56  Las Vegas
4    Max   21     Moscow
'''

grouped = df.groupby('Age').sum()
print(grouped)

'''
     Name       City
Age                 
21    Max     Moscow
27   John   New York
45   Anna          0
56   Alex  Las Vegas
'''