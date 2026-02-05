import numpy as np 
import pandas as pd

# # Load the data
# df = pd.read_csv("pd_hoa_activities.csv")
# print(df.shape)

# # Explore the data
# print(df.head(5))
# print(df.tail(7))

# print(f"Number of participants: {df.shape[0]//9}") # 9 is the number of tasks per pid

# print(df.iloc[660:670, :])

# # Missing data
# print(df["duration"].value_counts()["?"]) # returns each unique value and the amount of occurrences of it within a series

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

# # replaces a value with a specified value
# # inplace = True modifies dataframe instead of returning a modified one
# print()
# df.replace("?", np.NaN, inplace=True)

# # isnull() will return a bool array
# # representing true/false if value is null
# # sum() will count up each True per column
# # and return a series
# print(df.isnull().sum())

# df.dropna(inplace=True)
# print("After dropping:\n", df.isnull().sum())
# print(df.shape)

# # indexing might have been effected, lets check

# print(df.iloc[650:670, :])

# df.reset_index(inplace=True, drop=True)

# # old index is saved, we don't need it, add drop=True to reset_index
# print(df.head(3))



# # Decode task!
# # replace 1-8 and dot with more human readable/meaningful labels
# task_decoder = {"1": "Water Plants", "2": "Fill Medication Dispenser",
#                 "3": "Wash Countertop","4":"Sweep and Dust", "5": "Cook",
#                  "6": "Wash Hands","7": "Perform TUG", "8": "Perform TUG w/ Questions", "dot": "Day Out Task"}

# def decode_task(df):
#     ser = df["task"]
#     for key in task_decoder:
#         ser.replace(key, task_decoder[key], inplace=True)

# decode_task(df)
# print(df.head(10))


# # Clean Class
# # Lots of different ways that labels were encoded
# # want to convert them to only 2 different values

# print(df["class"].unique())

# def clean_class(df):
#     ser = df['class'].copy()
#     for i in range(len(ser)):
#         curr_class = str(ser.iloc[i])
#         curr_class = curr_class.lower()
#         if "hoa" in curr_class or "healthy" in curr_class:
#             ser.iloc[i] = "HOA"
#         elif "pd" in curr_class or "parkinson" in curr_class:
#             ser.iloc[i] = "PD"
#         else:
#             print(f"Unrecognized status: {i} {curr_class}")
#         df["class"] = ser

# clean_class(df)
# print(df.head(20))
# print(df["class"].value_counts())


# # Check Column Types
# for column in df.columns:
#     print(column, df[column].dtype)


# # logic error!! duration values are stored as strings
# # its concatanting a bunch of strings together!
# # print(df["duration"].mean())
# df["duration"] = df["duration"].astype(np.int32)

# for column in df.columns:
#     print(column, df[column].dtype)

# print(df["duration"].mean())
# print(df["duration"].sum())
# print(df["duration"].std())

# # We don't need to store the indexes
# df.to_csv("pd_hoa_activities_cleaned.csv", index=False)

# TODO: Try to analyze this data a bit
# do some group bys to compare each group
# compare each group's average duration
# compare each group's average duration per task
# try to find which person per class had the best and worst average duration over all tasks

# find the average duration per task given different age groups (may need to do some research online/chatbot). If you do, try to understand the methods that you find online. Then, try to use these methods to additional analysis yourself

