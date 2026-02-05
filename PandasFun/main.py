"""
======================================================
ATTRIBUTES
======================================================
1. what is the type
    e.g. how should it be stored?
    int, float, str, ...

2. what is the semantic type
    e.g. what does the attribute (and its values)
    represent?
    domain knowledge!!!

3. what is the measurement scale
Categorical 
    nominal: categorical without an inherent ordering
    ex: 
    - names
    - eye colors
    - occupations
    - zip codes, ...

    ordinal: categorical with an inherent ordering
    ex: 
    - T shirt sizes (...,S, M, L, ...)
    - letter grades (A, A-, B+, ...)

Continuous
    ratio-scaled: continuous where 0 means absence
    ex: 
    - 0lbs means an absence of weight
    - 0 degrees kelvin means absence of temperature

    interval: continuous where 0 does not mean absence
    - differences between values matter but ratios don't
    ex: 
    - 0 degrees fahrenheit does not mean absence of temp
    - latitude and longitude

======================================================
Noisy vs Invalid
======================================================
    Noisy: valid on the measurement scale, but recorded incorrectly
    ex: 
    - age attribute, someone who is 18 years old, but 81 years old was entered

    Invalid: not valid on the measurement scale
    ex: 
    - age attribute, someone enters "Sarah"

======================================================
Labeled vs Unlabeled Data (Preview for Machine Learning)
======================================================

Labeled data:
    If there is an attribute (called a "class" or "target") that you are interested in predicting for unseen instances, this is called supervised machine learning.

    Examples:
        - Email spam detection:
            data = email text, sender, number of links
            class = spam or not spam

        - House price prediction:
            data = square footage, bedrooms, location
            class = price in dollars

    If the class attribute is categorical (labels / categories), this is called a classification task.
        Examples: spam vs not spam, digit 0-9, disease yes/no

    If the class attribute is continuous (numeric),
    this is called a regression task.
        Examples: house price, temperature, exam score


Unlabeled data:
  There is no class attribute to predict. Instead, you are exploring the data to discover patterns.
  
  - The data still can have meaning and structure, it just lacks a target label we are trying to predict/discover

  Examples:
    - Grouping customers by purchasing behavior
    - Finding clusters of similar songs or movies
    - Discovering topics in news articles
    - Detecting unusual credit card transactions
    - Finding associations like "items often bought together"

  This is often called unsupervised learning or data mining.
"""



# PANDAS
# a data science library
# built on top of NumPy
# why pandas?
# lots of great built in data science functionality
# like indexing, slicing, cleaning, stats, ...
# major shortcomings of using 2D lists of tables
# 1. lack of label-based indexing
# 2. lot of work to grab a column

# 2 main data storage objects
# 1. 1D: Series
# 2. 2D: DataFrame (every column is a Series)

# lets start with Series
# you can create a Series from many different date types
# lets make one from a list
import pandas as pd
import numpy as np

# pops = [229447, 755078, 151574, 38977]
# cities = ["Spokane", "Seattle", "Bellevue", "Issaquah"]
# pop_ser = pd.Series(pops, index=cities)
# pop_ser.name = "Population"
# print(pop_ser)

# # indexing and slicing with series

# # first method: labels

# # 1. indexing with label
# print(pop_ser["Seattle"])
# # 2. indexing with list of labels
# print(pop_ser[["Seattle", "Issaquah"]])

# # 3. slicing with labels
# # is inclusive of the stop label
# print(pop_ser["Seattle":"Issaquah"])

# # second indexing with positions
# # use .iloc[ ] for position based indexing

# # 1. indexing with position
# print(pop_ser.iloc[1])

# # 2. indexing with list of positions
# print(pop_ser.iloc[[1, 3]])

# # 3. slicing with positions
# # is exclusive of the stop label
# print(pop_ser.iloc[1:3])

# # summary stats
# print(pop_ser.mean())
# print(pop_ser.std())
# # works with numpy ufuncs
# print(np.min(pop_ser))

# # we can add a new value to the series
# # much like we add a new key-value pair to a dictionary
# pop_ser["Sammamish"] = 65116
# print(pop_ser)

# # we can also make an empty Series
# pop_ser2 = pd.Series(dtype=int)
# pop_ser2["Federal Way"] = 97701
# print(pop_ser2)
# print()

# # time for DataFrames!
# # lets make a DataFrame from a 2D list
# twod_list = [["a", 3, 99.9],
#              ["b", 60, -12.1],
#              ["c", 1, 5.5555]]
# df = pd.DataFrame(twod_list,
#                   index=["row1", "row2", "row3"],
#                   columns=["col1", "col2", "col3"])

# df.index.name = "rows"
# df.columns.name = "cols"
# print(df)
# # task: make a dataframe for our city population data
# # columns: "City", "Population", "Size"
# # where Size is one of "Small", "Medium", "Large"
# pop_data = [["Spokane", 229447, "Large"],
#             ["Seattle", 755078, "Large"],
#             ["Bellevue", 151574, "Medium"],
#             ["Issaquah", 38977, "Small"]]
# pop_df = pd.DataFrame(pop_data, columns=["City", "Population", "Size"])
# pop_df = pop_df.set_index("City")
# print(pop_df)
# print()


# # Dataframe indexing
# print("=========DF index=========")
# # option 1: Basic Indexing (Takes column name, not row index)
# # df[col_name1] 
# print(pop_df["Population"])
# # df[[col_name1, col_name2]] 
# print(pop_df[["Population", "Size"]])

# print("=========DF .loc=========")
# # Option 2: .loc function (takes row/column names, not positions)
# # format df.loc[row, col]
# # each section can take 
# #   - single value (row/cell selection)
# print(pop_df.loc["Seattle"])
# print(pop_df.loc["Seattle", "Population"])
# #   - slice
# print(pop_df.loc[:, "Population"])
# print(pop_df.loc["Seattle":"Issaquah", "Population"])
# print(pop_df.loc["Seattle":"Issaquah", "Population":"Size"])
# #   - fancy index (list of values)
# print(pop_df.loc[["Seattle","Issaquah"], "Population"])

# print("=========DF .iloc=========")
# # Option 3: .iloc function (takes, row/column positions, not names)
# print(pop_df.iloc[1])
# print(pop_df.iloc[1, 0])
# #   - slice
# print(pop_df.iloc[:, 0])
# print(pop_df.iloc[1:3, 0])
# print(pop_df.iloc[1:3, 0:2])
# #   - fancy index (list of values)
# print(pop_df.iloc[[1,3], 0])



# # Reading in a CSV
# # lets load up regions.csv into a dataframe

# region_df = pd.read_csv("regions.csv", index_col=0)
# print(region_df)
# print(region_df.columns)
# print(region_df.index)

# # now lets join pop_df and region_df on "City"
# # to make a 3rd DataFrame
# # by default, merge() does an inner join
# print(pop_df.index.name)
# merged_df = pop_df.merge(region_df, on="City", how="outer")
# print(merged_df)

# # lets write the contents of merged_df to a file
# # merged.csv
# merged_df.to_csv("merged.csv")

# # data aggregation
# # gathering and presenting data in a summarized form
# # lets see split apply combine in action!
# # 1. split
# grouped_by_size = merged_df.groupby("Size")

# # short way to do # 2. apply and #3. combine
# # grouped operations return a series with each group item 
# # matched to the corresponding value
# mean_pop_ser = grouped_by_size["Population"].mean()
# print("short way: split apply combine results:")
# print(mean_pop_ser)
# print()




# # longer way to do #2. apply and #3. combine
# # (explaining what is going on with grouped_by_size)
# print(grouped_by_size)
# print(grouped_by_size.groups.keys())
# large_df = grouped_by_size.get_group("Large")
# print(large_df)
# print(type(large_df))
# # we don't want to hard code extracted each attribute value's
# # data frame with get_group()
# # instead, we are going to write extensible code using...
# # a loop!!
# mean_pop_ser = pd.Series(dtype=float)
# for group_name, group_df in grouped_by_size:
#     print(group_name)
#     print(group_df)
#     # 2. apply
#     group_pop_ser = group_df["Population"]
#     group_pop_mean = group_pop_ser.mean()
#     print(group_pop_mean)
#     # 3. combine
#     mean_pop_ser[group_name] = group_pop_mean
#     print("*****")

# print("long way: split apply combine results:")
# print(mean_pop_ser)

