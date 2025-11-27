import pandas as pd

df = pd.read_csv('info.csv')

print(df.head())

'''
Начальные данные

Date, Product, Sales, Revenue
2023-01-01, Product A, 100, 1000
2023-01-02, Product B, 150,1500
2023-01-03, Product C, NaN, 2000
2023-01-04, Product A, 120, 1200
2023-01-05, Product B, 130,1300
2023-01-06, Product A, NaN, NaN
'''

'''
Конечные данные

         Date     Product  Sales  Revenue
0  2023-01-01   Product A    100     1000
1  2023-01-02   Product B    150     1500
2  2023-01-03   Product C    NaN     2000
3  2023-01-04   Product A    120     1200
4  2023-01-05   Product B    130     1300
'''

filter_df = df[df[' Product'] == ' Product A']
print(filter_df)

'''
         Date     Product  Sales   Revenue
0  2023-01-01   Product A    100    1000.0
3  2023-01-04   Product A    120    1200.0
5  2023-01-06   Product A    NaN       NaN
'''

filter_df.to_csv("nex_info.csv", index=False)

'''
Такие данные сохраняет в новый файл

Date, Product, Sales, Revenue
2023-01-01, Product A, 100,1000.0
2023-01-04, Product A, 120,1200.0
2023-01-06, Product A, NaN,
'''