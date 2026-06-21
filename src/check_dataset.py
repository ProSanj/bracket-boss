import pandas as pd

df = pd.read_csv(
    "data/results.csv",
    encoding="latin1"
)

print(df.head())
print()
print(df.tail())
print()
print("Rows:", len(df))