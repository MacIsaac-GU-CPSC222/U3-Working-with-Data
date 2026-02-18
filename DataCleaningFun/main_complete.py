import numpy as np 
import pandas as pd

# Load the data
df = pd.read_csv("pd_hoa_activities.csv")
print(df.shape)

# Explore the data
print(df.head(5))
print(df.tail(7))

print(f"Number of participants: {df.shape[0]//9}") # 9 is the number of tasks per pid

print(df.iloc[660:670, :])

# Missing data
print(df["duration"].value_counts()["?"]) # returns each unique value and the amount of occurrences of it within a series

# ways to handle missing values
# 1. discard them
# never want to throw away data
# 2. fill them
# fill w/ most frequent label
# fill w/ central tendency measure
# 3. do nothing with them
# handle on a case by case basis later

# replace "?" with np.NaN
# support in np for NaN values!
# fill NaN, drop NaN, etc

# replaces a value with a specified value
# inplace = True modifies dataframe instead of returning a modified one
print()
df.replace("?", np.NaN, inplace=True)

# isnull() will return a bool array
# representing true/false if value is null
# sum() will count up each True per column
# and return a series
print(df.isnull().sum())

df.dropna(inplace=True)
print("After dropping:\n", df.isnull().sum())
print(df.shape)

# indexing might have been effected, lets check

print(df.iloc[650:670, :])

df.reset_index(inplace=True, drop=True)

# old index is saved, we don't need it, add drop=True to reset_index
print(df.head(3))



# Decode task!
# replace 1-8 and dot with more human readable/meaningful labels
task_decoder = \
    {"1": "Water Plants", 
     "2": "Fill Medication Dispenser",
     "3": "Wash Countertop",
     "4":"Sweep and Dust", 
     "5": "Cook",
     "6": "Wash Hands",
     "7": "Perform TUG", 
     "8": "Perform TUG w/ Questions", 
     "dot": "Day Out Task"}

def decode_task(df):
    ser = df["task"]
    for key in task_decoder:
        ser.replace(key, task_decoder[key], inplace=True)

decode_task(df)
print(df.head(10))


# Clean Class
# Lots of different ways that labels were encoded
# want to convert them to only 2 different values

print(df["class"].unique())

df.replace(["healthy", "hoa", "HOA"], "HOA", inplace=True)
df.replace(["PD", "parkinson's", "Parkinson's", "Parkinson", "pd"], "PD", inplace=True)

print(df.head(20))
print(df["class"].value_counts())


# Check Column Type

def check_types(df):
    for column in df.columns:
        print(column, df[column].dtype)
    print()
check_types(df)

# Get mean of duration
#   - logic error!! duration values are stored as strings
#   - its concatenating a bunch of strings together!
# print(df["duration"].mean())


# change type of data in a column/series
df["duration"] = df["duration"].astype(np.int32)

check_types(df)


# get mean, sum, std of duration
print(df["duration"].mean())
print(df["duration"].sum())
print(df["duration"].std())

# Save our work (to_csv, no index)
#   - We don't need to store the indexes
df.to_csv("pd_hoa_activities_cleaned.csv", index=False)

# TODO: Try to analyze this data a bit
# do some group bys to compare each group
# compare each group's average duration
# compare each group's average duration per task
# try to find which person per class had the best and worst average duration over all tasks

# find the average duration per task given different age groups (may need to do some research online/chatbot). If you do, try to understand the methods that you find online. Then, try to use these methods to additional analysis yourself


# =========== Dates Demo ===========

# Load CSV

# Without Dates (just strings)
df = pd.read_csv("dates.csv")

# FIXED!
df = pd.read_csv("dates.csv", parse_dates=["date"], date_format="%m-%d-%Y")

print(df.dtypes)

# Set Index
df.set_index("date", inplace=True)

print(df.head())

print("Date Index sorted?", df.index.is_monotonic_increasing)

# Try slicing BEFORE sorting (often errors for partial/range slicing)
# print(df.loc["11-05-2025":"02-12-2026"])


# Sort Index
df_sorted = df.sort_index()

print("Date Index sorted?", df_sorted.index.is_monotonic_increasing)

print(df_sorted.head())

print()


# Between Nov 11 2025 and Feb 12 2026
print(df_sorted.loc["2025-11-05":"2026-02-12"])
print()


# All rows after jan 2026
print(df_sorted.loc["2026-02-01":])
print()

# Feb 12 2026
print(df_sorted.loc["2026-02-12"])
print()




