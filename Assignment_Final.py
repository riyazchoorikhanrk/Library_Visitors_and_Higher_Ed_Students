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


# Read the data using pandas
data = {
    'Category': ['Female Full-time', 'Female Part-time', 'Female Total',
                 'Male Full-time', 'Male Part-time', 'Male Total',
                 'Total Full-time', 'Total Part-time', 'Grand Total'],
    'Postgraduate': [283, 982, 1265, 158, 690, 848, 441, 1672, 2113],
    'First Degree': [5656, 1577, 7233, 3916, 843, 4759, 9572, 2420, 11992],
    'Other Undergraduate': [20545, 56371, 76916, 21508, 55968, 77476, 42053, 112339, 154392],
    'Total': [66043, 93298, 159341, 75570, 91956, 167526, 141613, 185254, 326867],
}

df = pd.DataFrame(data)


def plot_bar(dataframe, category, title, x_label, y_label):
    """
    Plots a bar chart for a specific category.

    Parameters:
    - dataframe: Pandas DataFrame containing the data.
    - category: String, the category to plot (e.g., 'Female Full-time').
    - title: String, the title of the plot.
    - x_label: String, the label for the x-axis.
    - y_label: String, the label for the y-axis.
    """
    subset = dataframe[dataframe['Category'] == category]
    subset = subset.set_index('Category').transpose()
    subset.plot(kind='bar', legend=False)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


plot_bar(df, 'Female Full-time', 'Female Full-time Students',
         'Degree Level', 'Number of Students')
plot_bar(df, 'Male Part-time', 'Male Part-time Students',
         'Degree Level', 'Number of Students')
plot_bar(df, 'Total Full-time', 'Total Full-time Students',
         'Degree Level', 'Number of Students')
