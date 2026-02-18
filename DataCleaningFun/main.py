import numpy as np 
import pandas as pd

# # Load the data
df = pd.read_csv("pd_hoa_activities.csv")
print(df.shape)
# Explore the data (head and tail)
print(df.head(5))
print(df.tail(7))

# unique participants
print(len(df["pid"].unique()))

# look at missing data (rows 660-670)

print(df.iloc[660:670])

# # Missing data
# # .value_counts() returns each unique value and the amount of occurrences of it within a series
# # call on duration, look at "?""

print(df["duration"].value_counts()["?"])

# # ways to handle missing values
# # 1. discard them
# # never want to throw away data

# # 2. fill them
# # fill w/ most frequent label
# # fill w/ central tendency measure
# # 3. do nothing with them
# # handle on a case by case basis later

# # replace "?" with np.NaN
# # support in np for NaN values!
# # fill NaN, drop NaN, etc
df.replace("?", np.NaN, inplace=True)
# print(df["duration"].value_counts()["?"])

# # replaces a value with a specified value
# # inplace = True modifies dataframe instead of returning a modified one
# print()

# df.replace("?", np.NaN, inplace=True)

# # isnull() will return a bool array
# # representing true/false if value is null
# # sum() will count up each True per column
# # and return a series
print(df.isnull().sum())
print(df.shape)

df.dropna(inplace=True)

print("After dropping:\n", df.isnull().sum())
print(df.shape)

# # indexing might have been effected, lets check

print(df.iloc[650:670, :])

df.reset_index(inplace=True, drop = True)
print(df.iloc[650:670, :])
# # old index is saved, we don't need it, add drop=True to reset_index
# print(df.head(3))



# # Decode task!
# # replace 1-8 and dot with more human readable/meaningful labels
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


# Clean Class
# Lots of different ways that labels were encoded
# want to convert them to only 2 different values


# Check Column Types


# Get mean of duration


# change type of data in a column/series


# get mean, sum, std of duration


# Save our work (to_csv, no index)




# =========== Dates Demo ===========

# Load CSV


# Set Index


# Check Sorted


# Try slicing


# Sort Index


# Between Nov 11 2025 and Feb 12 2026


# All rows after jan 2026


# Feb 12 2026





# ===== end of class practice time =====
# TODO: Try to analyze this data a bit

# do some group bys to compare each  (try to do atleast two different ones)

#   - compare each group's average duration

#   - compare each group's average duration per task

#   - try to find which person per class had the best and worst average duration over all tasks










# find the average duration per task given different age groups (may need to do some research online/chatbot). If you do, try to understand the methods that you find online. Then, try to use these methods to additional analysis yourself

