import pandas as pd

file = "titanic1.csv"
df = pd.read_csv(file)

df.columns = df.columns.str.lower()

df_cleaned = df.dropna(subset=['cabin'])

print(f"Passengers with cabin numbers recoded: {len(df_cleaned)}")
print(f"Amount that survived: {df_cleaned['survived'].sum()}")