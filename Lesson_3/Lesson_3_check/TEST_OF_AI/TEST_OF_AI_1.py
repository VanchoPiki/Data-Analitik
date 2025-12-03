"""
Задание 1: Анализ данных сотрудников (Базовое)

Цель: Закрепить создание DataFrame, выбор данных, базовую статистику и обработку пропусков.

Задача:
Создайте DataFrame employees со следующими данными о сотрудниках:

ID: [101, 102, 103, 104, 105]
Name: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
Department: ['Sales', 'IT', 'Sales', 'HR', 'IT']
Salary: [50000, 75000, 48000, None, 62000]
Experience (лет): ['5', '8', '3', '10', '7']
Требуется выполнить следующие шаги:

Вывести первые 3 строки DataFrame.
Вывести общую информацию о данных (info).
Показать базовую статистику для числовых колонок (describe). Почему колонка Salary не отображается корректно в статистике?
Обработка данных: Заменить пропущенное значение в колонке Salary на среднюю зарплату по оставшимся сотрудникам (подсказка: сначала преобразуйте Salary в float, посчитайте среднее df['Salary'].mean(), затем используйте fillna).
Преобразовать колонку Experience из строкового типа в целочисленный (int).
Вывести имена всех сотрудников из отдела 'IT', используя фильтрацию.
"""

import pandas as pd
data = {
    "ID" : [101, 102, 103, 104, 105],
    "Name" : ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    "Department" : ['Sales', 'IT', 'Sales', 'HR', 'IT'],
    "Salary" : [50000, 75000, 48000, None, 62000],
    "Experience (лет)" : ['5', '8', '3', '10', '7']
}
def string_3(df):
    df_3_string = df.head(3)
    return df_3_string

def data_info(df):
    df_info = df.info
    return df_info

def describe_df(df):
    df_ds = df.describe()
    return df_ds

def dont_NaN(df):
    df['Salary'] = df['Salary'].astype(float)
    df_mean = df['Salary'].mean()
    df.fillna(df_mean, inplace=True)
    df['Salary'] = df['Salary'].astype(int)
    return df

def experiance(df):
    df['Experience (лет)'] = df['Experience (лет)'].astype(int)
    return df

def Name(df):
    df_name = df['Name']
    return df_name

df = pd.DataFrame(data)
print(experiance(df))