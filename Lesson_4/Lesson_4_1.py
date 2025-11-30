import pandas as pd

data = {
    'Age' : [34, 37, 13, 64, 37, 47, 24, 38, 26, 41, 19, 51, 44]
}

df = pd.DataFrame(data)

mean_age = df['Age'].mean()
print(mean_age)

median_age = df['Age'].median()
print(median_age)

mode_age = df['Age'].mode()[0]
print(mode_age)

variance_age = df['Age'].var()
std_age = df['Age'].std()
print(variance_age, std_age)

quantities_age = df['Age'].quantile([0.25, 0.5, 0.75])
persentile_age = df['Age'].quantile(0.9)
print(quantities_age, persentile_age)