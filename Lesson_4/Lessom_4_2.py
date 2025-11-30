from scipy import stats

ages = [34, 37, 13, 64, 37, 47, 24, 38, 26, 41, 19, 51, 44]

t_stat, p_value = stats.ttest_1samp(ages, popmean=30)
print(t_stat, p_value)
