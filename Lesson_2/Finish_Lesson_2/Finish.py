import numpy as np

arr = np.array(list)
print(arr * 2) # - умножает каждый элемент в списке на 2

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8,9],
])
print(matrix * 2) # - умножает каждый элемент в матрице на 2

zeros = np.zeros((3,4))
print(zeros) # - выводится матрица со всеми значениями = 0 (размерами 3 на 4)

ones = np.ones((2, 3))
print(ones) # - выводится матрица со всеми значениями = 1 (размерами 2 на 3)

eye = np.eye(4)
print(eye) # - выводится матрица в которой по диагонали указанное количество единиц

linspace = np.linspace(0, 10, 15)
print(linspace) # - выводится матрица с распределенными числами от 0 до 10 в кол-ве 15 шт

arangee = np.arange(0, 10, 3)
print(arangee) # - выводит список от 0 до 10 с шагом 3

arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4]) # - обычный срез

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix[1:, :2]) # -выводит первую строку и в этой строке начала до 2-ого элемента

arr = np.arange(1, 13)
print(arr) # - выводит список от 1 до 12

reshape = arr.reshape((3, 4))
print(reshape) # - выводит матрицу с 3 строками и 4 столбцами =>

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

hstack = np.hstack((arr1, arr2))
print(hstack) # - соединяет 2 списка по горизонтали

vstack = np.vstack((arr1, arr2))
print(vstack) # - соединяет 2 списка по вертикали

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

hsplit = np.hsplit(matrix, 2)
print(hsplit) # - разделяет матрицу на 2 матрицы

vsplit = np.vsplit(matrix, 2)
print(vsplit) # - разделяет матрицу на 2 списка

arr = np.array([1, 2, 3, 4])

print(np.mean(arr)) # - находит среднюю арифметическую у списка

print(np.std(arr)) # - выводит стандартное отклонение элементов массива

print(np.median(arr)) # - выводит медиану массива

print(np.min(arr), np.max(arr)) # - выводит максимальное и минимальное значение в массиве