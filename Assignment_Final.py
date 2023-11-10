# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:48:08 2023

@author: riyaz
"""

# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('library_users_by_age_cleaned.csv')


def median_function_to_cal(df):
    # Calculate the median for the "Age18-59" column
    average_people = np.median(df["Age18-59"])
    print("Median Age 18-59:", average_people)


# Call the median_function_to_cal function with the DataFrame df
median_function_to_cal(df)

# Calculate a new column "total_12" by summing all age groups
df["total_12"] = df["Age18-59"] + df["Age60-100"] + df["Age0-4"] \
    + df["Age5-11"] + df["Age12-17"]

# Plot the data
plt.figure()
plt.plot(df["Age0-4"], df["Library"], label="Age 0 - 4")
plt.plot(df["Age12-17"], df["Library"], label="Age 12 - 17")
plt.plot(df["Age18-59"], df["Library"], label="Age 18 - 59")
plt.plot(df["Age60-100"], df["Library"], label="Age 60 - 100")

plt.legend()
plt.grid()

xlab = "Number of people"
ylab = "Libraries"
xtitle = "Library Visitors Data"

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(xtitle)

# Show the plot
plt.show()
df = pd.read_csv('library_users_by_age_cleaned.csv')


def median_function_to_cal(df):
    # Calculate the median for the "Age18-59" column
    average_people = np.median(df["Age18-59"])
    print("Median Age 18-59:", average_people)


# Call the median_function_to_cal function with the DataFrame df
median_function_to_cal(df)

# Calculate a new column "total_12" by summing all age groups
df["total_12"] = df["Age18-59"] + df["Age60-100"] + df["Age0-4"] \
    + df["Age5-11"] + df["Age12-17"]

# Plot the data
plt.figure()
plt.scatter(df["Age0-4"], df["Library"], label="Age 0 - 4")
plt.scatter(df["Age12-17"], df["Library"], label="Age 12 - 17")
plt.scatter(df["Age18-59"], df["Library"], label="Age 18 - 59")
plt.scatter(df["Age60-100"], df["Library"], label="Age 60 - 100")

plt.legend()
plt.grid()

xlab = "Number of people"
ylab = "Libraries"
xtitle = "Library Visitors Data"

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(xtitle)

# Show the plot
plt.show()




# Create a DataFrame with the provided data
data = {
    'Institution': ['FE Institutions', 'HE Institutions'] * 4,
    'Gender': ['Female', 'Female', 'Male', 'Male'] * 2,
    'Coursetype': ['Full-time', 'Part-time'] * 4,
    'Postgraduate': [283, 982, 158, 690, 66043, 93298, 75570, 91956],
    'First Degree': [5656, 1577, 3916, 843, 464349, 49095, 435345, 35608],
    'Other Undergraduate': [20545, 56371, 21508, 55968, 72366, 161856, 47933, 108795],
}

df = pd.DataFrame(data)

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data with 'hue' parameter
df.set_index(['Institution', 'Gender']).plot(kind='bar', ax=ax, rot=45, colormap='viridis', edgecolor='black', linewidth=0.7)

# Customize the plot
plt.title('Number of Students in FE and HE Institutions by Gender and Course type')
plt.xlabel('Institution and Gender')
plt.ylabel('Number of Students')
plt.legend(title='Degree Level')

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()
