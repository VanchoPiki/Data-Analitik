import numpy as np

# Дан массив температур за неделю: [22.5, 24.0, 19.5, 25.5, 23.0, 20.5, 21.0]
# 1. Создайте массив и найдите:
#    - Среднюю температуру за неделю
#    - Медиану температур
#    - Стандартное отклонение
#    - День с максимальной и минимальной температурой
# 2. Создайте массив с пропущенными данными (замените 2 значения на NaN)
# 3. Найдите среднюю температуру, игнорируя пропущенные значения
# 4. Замените NaN на среднее значение остальных температур

temp = [22.5, 24.0, 19.5, 25.5, 23.0, 20.5, 21.0]

mean_temp = np.mean(temp)
median_temp = np.median(temp)
std_temp = np.std(temp)
min_temp = np.min(temp)
max_temp = np.max(temp)

print(f"Средняя температура за неделю: {mean_temp}\n\n Медиану температур: {median_temp}\n\n Стандартное отклонение: {std_temp}\n\n Минимальная: {min_temp}\n\n Максимальное: {max_temp}\n")

temp_2 = [22.5, 24.0, None, 25.5, 23.0, None, 21.0]
temp_2_2 = []
def main(temp_2):
    temp_2_2 = []
    for i in temp_2:
        if i is not None:
            temp_2_2.append(i)
    for i in temp_2:
        if i is None:
            i = np.mean(temp_2_2)
            temp_2_2.append(float(i))
        return temp_2_2

print(main(temp_2))