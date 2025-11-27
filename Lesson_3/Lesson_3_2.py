import pandas as pd

data = {
    'Name' : ['John', 'Anna', 'Peter', 'Alex'],
    'Age' : ['27', '45', '56', '21'],
    'City' : ['New York', 'Florida', 'Las Vegas', 'Moscow']
}

df = pd.DataFrame(data)

print(df.head())

"""
    Name Age       City
0   John  27   New York
1   Anna  45    Florida
2  Peter  56  Las Vegas
3   Alex  21     Moscow
"""

print(df.tail())

"""
    Name Age       City
0   John  27   New York
1   Anna  45    Florida
2  Peter  56  Las Vegas
3   Alex  21     Moscow
"""

print(df.describe())

"""
        Name Age      City
count      4   4         4
unique     4   4         4
top     John  27  New York
freq       1   1         1

"""

print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    4 non-null      object
 1   Age     4 non-null      object
 2   City    4 non-null      object
dtypes: object(3)
memory usage: 228.0+ bytes
None
"""