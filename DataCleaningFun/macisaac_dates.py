import pandas as pd
# =========== Dates Demo ===========


# two ways to get datetime
# 1. When reading in data
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

df = pd.read_csv("dates.csv", parse_dates=["date"], date_format="%m-%d-%Y")

# 2. convert data
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
df = pd.read_csv("dates.csv")
df["date"] = pd.to_datetime(
    df["date"],
    format="%m-%d-%Y"
)
print(df.dtypes)

# # Set Index
df.set_index("date", inplace=True)

print(df.head())

print("Date Index sorted?", df.index.is_monotonic_increasing)

# # Try slicing BEFORE sorting (often errors for partial/range slicing)
# print(df.loc["11-05-2025":"02-12-2026"])


# # Sort Index
df_sorted = df.sort_index()

print("Date Index sorted?", df_sorted.index.is_monotonic_increasing)

print(df_sorted.head())

# print()


# # Between Nov 11 2025 and Feb 12 2026
print(df_sorted.loc["2025-11-05":"2026-02-12"])
# print()


# # All rows after jan 2026
print(df_sorted.loc["2026-02-01":])
# print()

# # Feb 12 2026
print(df_sorted.loc["2026-02-12"])
# print()