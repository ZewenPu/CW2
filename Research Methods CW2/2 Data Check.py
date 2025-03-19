import pandas as pd
import numpy as np
import os

# Reading data
data = pd.read_csv("1 Data Filtering.csv")

# Define the mapping relationship between different age groups and numbers
age_range = {
    "20-29": 1,  # young
    "30-39": 2,  # youth
    "40-49": 3,  # middle-aged
    "50-59": 3,  # middle-aged
    "60-69": 4,  # elderly
    "70-79": 4   # elderly
}

# Add an ID column and insert it into the first column
data.insert(0, "ID", data["age_group"].map(age_range))

# Delete the rows where mapping failed (if have)
data = data.replace([np.inf, -np.inf], np.nan).dropna(subset=["ID"])

# Sort the ID column by age in ascending order
data_sorted = data.sort_values(by="ID").reset_index(drop=True)

# Save the processed data on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, "2 Data Check.csv")
data_sorted.to_csv(output_file, index=False)

print(data_sorted.head())
print("-" * 90)
print(f"Successfully saved to desktop：{output_file}")

