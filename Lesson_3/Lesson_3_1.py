import pandas as pd

data = {
    'Name' : ['John', 'Anna', 'Peter', 'Alex'],
    'Age' : ['27', '45', '56', '21'],
    'City' : ['New York', 'Florida', 'Las Vegas', 'Moscow']
}

df = pd.DataFrame(data)

print(df)

'''     Name  Age      City
    0   John  28   New York
    1   Anna  45    Florida 
    2  Peter  56  Las Vegas
    3   Alex  21     Moscow  '''

print(df['Name'])

'''     0     John
        1     Anna
        2    Peter
        3     Alex
        Name: Name, dtype: object       '''

print(df.loc[0])

'''     Name        John
        Age           28
        City    New York
        Name: 0, dtype: object      '''