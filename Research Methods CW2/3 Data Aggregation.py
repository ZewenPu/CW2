import pandas as pd
import os

# Reading data
data = pd.read_csv("2 Data Check.csv")

# Group by age (ID) and diet type (diet_group) and calculate the mean for each group
aggregated = data.groupby(['ID', 'diet_group'], as_index=False).agg({
    'mean_ghgs': 'mean',
    'mean_land': 'mean',
    'mean_watscar': 'mean'
})

# Sort ascending
aggregated = aggregated.sort_values(by='ID')

# Save the processed data on the desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop, "3 Data Aggregation.csv")
aggregated.to_csv(output_file, index=False)

print(aggregated.head())
print("-" * 90)
print(f"Successfully saved to desktop：{output_file}")

