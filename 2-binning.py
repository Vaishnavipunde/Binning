# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:33:49 2023

@author: sai
"""
import pandas as pd

# Load the dataset 'ethnic.csv' into a DataFrame 'df'
df = pd.read_csv("C:/2-dataset/ethnic.csv")

# Display the first five rows of the DataFrame
df.head()

# Get information about the DataFrame 
df.info()

# Create a new column 'Salaries_new' based on bins defined by minimum, mean, and maximum salary values
df["Salaries_new"] = pd.cut(df["Salaries"], bins=[min(df.Salaries), df.Salaries.mean(), max(df.Salaries)], labels=['low', 'high'])

# Display the counts of each category in the 'Salaries_new' column
df["Salaries_new"].value_counts()

# Create a new column 'Salaries_new' based on quantiles of 'Salaries'
df["Salaries_new"] = pd.cut(df["Salaries"], bins=[min(df.Salaries), df.Salaries.quantile(0.25), df.Salaries.mean(), df.Salaries.quantile(0.75), max(df.Salaries)], labels=["g1", "g2", "g3", "g4"])

# Display the counts of each category in the 'Salaries_new' column based on quartiles
df["Salaries_new"].value_counts()
