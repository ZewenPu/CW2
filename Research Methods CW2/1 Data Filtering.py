import pandas as pd
import os

# Reading raw data
data = pd.read_csv("Results_21MAR2022_nokcaladjust.csv")

# Select the 5 columns
data = data[["age_group", "diet_group", "mean_ghgs", "mean_land", "mean_watscar"]]

# Check if there are missing values and print the number
print("Number of missing values:")
print(data.isnull().sum().to_string())
print("-" * 90)

# Delete rows with missing data
data_clean = data.dropna()

# Save the preprocessed data on the desktop
output_file = os.path.expanduser("~/Desktop/1 Data Filtering.csv")
data_clean.to_csv(output_file, index=False)

print(data_clean.head())
print("-" * 90)
print(f"File successfully saved to: {output_file}")
