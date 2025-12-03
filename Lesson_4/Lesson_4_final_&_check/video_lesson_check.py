import pandas as pd
from scipy import stats


data = {
    'City_A' : [23, 53, 25, 74, 35, 54, 47, 21, 17, 46, 43],
    'City_B' : [37, 38, 71, 42, 17, 19, 27, 35, 23, 38, 44]
}

df = pd.DataFrame(data)

mean_age_A = df['City_A'].mean()
median_age_A = df['City_A'].median()
mode_A = df['City_A'].mode()[0]
variance_age_A = df['City_A'].var()
std_age_A = df['City_A'].std()

print(f"mean A : {mean_age_A}\n median A : {median_age_A}\n mode A : {mode_A}\n variance : {variance_age_A}\n std : {std_age_A}\n\n\n")

mean_age_B = df['City_B'].mean()
median_age_B = df['City_B'].median()
mode_B = df['City_B'].mode()[0]
variance_age_B = df['City_B'].var()
std_age_B = df['City_B'].std()

print(f"mean A : {mean_age_B}\n median A : {median_age_B}\n mode A : {mode_B}\n variance : {variance_age_B}\n std : {std_age_B}\n\n\n")

t_stat, p_value = stats.ttest_ind(df['City_A'], df['City_B'])
print(t_stat, p_value)

"""
mean A : 39.81818181818182
 median A : 43.0
 mode A : 17
 variance : 304.3636363636364
 std : 17.446020645512156



mean A : 35.54545454545455
 median A : 37.0
 mode A : 38
 variance : 223.2727272727273
 std : 14.94231331731226



0.6169275374726553 0.5442423873688744
"""