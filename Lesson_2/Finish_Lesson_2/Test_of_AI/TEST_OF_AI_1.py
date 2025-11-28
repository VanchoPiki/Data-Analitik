import numpy as np

# 1. Создайте массив чисел от 0 до 24
# 2. Преобразуйте его в матрицу 5x5
# 3. Умножьте все элементы на 3
# 4. Создайте вторую матрицу 5x5 со случайными числами от 1 до 10
# 5. Сложите две матрицы
# 6. Разделите результат на 2
# 7. Найдите минимальное и максимальное значение в финальной матрице

data = np.arange(0, 25, 1)
print(data, end='\n\n\n')
print(data.reshape(5, 5), end='\n\n\n')
print(data.reshape(5, 5) * 3, end='\n\n\n')

data_2 = np.array([
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 0, 1, 2, 3],
    [4, 5, 6, 7, 8],
    [9, 10, 0, 1, 2]
])

print(data_2, end='\n\n\n')
data_3 = data.reshape(5, 5) * 3 + data_2
print(data_3, end='\n\n\n')
data_4 = data_3 / 2
print(data_4, end='\n\n\n')
print(np.min(data_4), np.max(data_4))