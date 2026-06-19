import pandas as pd

file = "titanic1.csv"
df = pd.read_csv(file)

df.columns = df.columns.str.lower()
result = df.groupby(["sex", "pclass"])["survived"].sum()

print(result)

# Bonus: count non-survived by count - sum
result_not_survived = df.groupby(["sex", "pclass"])["survived"].count() - result

print(result_not_survived)

# Bonus: count non-survived by filter first, group after
died_df = df[df["survived"] == 0]
result_died = died_df.groupby(["sex", "pclass"]).size()
print(result_died)