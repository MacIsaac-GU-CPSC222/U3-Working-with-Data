import numpy as np 
import pandas as pd

df = pd.read_csv("pd_hoa_activities.csv")
print(df.shape)

# Exploring the dataset
print(df.head(5))
print(df.tail(7))

# unique participants
unique_pid = df["pid"].unique()
print(unique_pid)
print(len(unique_pid))


# look at missing data
print(df.iloc[660:670])
rows_with_qm = df["duration"] == "?"
print(rows_with_qm.iloc[660:670])

print(df.loc[rows_with_qm])


# Missing Data
# .value_counts() -> return each unique value and the amount of occurrences of it within a series

print(df["duration"].value_counts()["?"])


# Ways to handle missing values

# 1. Discard them
# - never want to throw away data
# - simplest way to deal with them
# - works well when you have lots of data and not much missing data

# 2. Fill them
# - fill w/ most frequent label
# - fill w/ central tendency measure

# 3. Do Nothing with them
# - handle on a case by case basis later


# Replace "?" with np.NaN
# NumPy give us support for np.NaN values
# - fill NaN, drop NaN, etc.

# replace method
# - replace a value with a specified value
# - inplace = True -> modifies the dataframe instead of returning a modified one

df.replace("?", np.nan, inplace=True)
print("?" in df["duration"].value_counts())

# isnull() will return a bool array
# represent true/value if value is null
# sum() will count up each True per column
# and return a series

print(df.isnull().sum())
print(df.shape)

df.dropna(inplace=True)
print(df.isnull().sum())
print(df.shape)

print(df.iloc[650:670])

df.reset_index(inplace=True, drop=True)
print(df.iloc[650:670])


# # Decode task!
# # replace 1-8 and dot with more human readable/meaningful labels
task_decoder = {
    "1": "Water Plants", 
    "2": "Fill Medication Dispenser",
    "3": "Wash Countertop",
    "4": "Sweep and Dust", 
    "5": "Cook",
    "6": "Wash Hands",
    "7": "Perform TUG", 
    "8": "Perform TUG w/ Questions", 
    "dot": "Day Out Task"}







# ===== end of class practice time =====
# TODO: Try to analyze this data a bit

# do some group bys to compare each  (try to do atleast two different ones)

#   - compare each group's average duration

#   - compare each group's average duration per task

#   - try to find which person per class had the best average duration over all tasks (then find the person per class with the worst)


# find the average duration per task given different age groups (may need to do some research online/chatbot). If you do, try to understand the methods that you find online. Then, try to use these methods to additional analysis yourself

