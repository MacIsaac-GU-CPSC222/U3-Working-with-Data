import pandas as pd
import numpy as np

# two ways to get datetime
# 1. When reading in data
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

# df = pd.read_csv("dates.csv", parse_dates=["date"], date_format="%m-%d-%Y")
# print(df.dtypes)
# 2. convert data
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html

df = pd.read_csv("dates.csv")
df["date"] = pd.to_datetime(df["date"], format="%m-%d-%Y")
print(df.dtypes)

df.set_index("date", inplace=True)
print(df.head())

print("Date sorted? ", df.index.is_monotonic_increasing)

df_sorted = df.sort_index()
print("Date sorted? ", df_sorted.index.is_monotonic_increasing)
print(df_sorted.loc["11-05-2025":"02-12-2026"])


print(df_sorted.loc["03-03-2026"])

# all rows after jan 2026
print(df_sorted.loc["2026-02-01":])