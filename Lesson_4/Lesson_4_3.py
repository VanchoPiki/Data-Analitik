from scipy import stats

group_1 = [23, 25, 31, 35, 45]
group_2 = [45, 51, 61, 35, 23]

stat, p_value = stats.mannwhitneyu(group_1, group_2)
print(stat, p_value)

"""      6.5             0.24625169969252703         """

""" Если Р значение маленькое, то значение между группами значимое """