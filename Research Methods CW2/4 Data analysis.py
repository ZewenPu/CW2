import pandas as pd

# Loading aggregated data
da = pd.read_csv("3 Data Aggregation.csv")

# Describe the current statistics
print("Overall statistics：")
print(da[['mean_ghgs', 'mean_land', 'mean_watscar']].describe().to_string())
print("-" * 60)

print("\nMean value of environmental impact for each group：")
age_stats = da.groupby('ID')[['mean_ghgs', 'mean_land', 'mean_watscar']].mean()
print(age_stats)
print("-" * 60)

print("\nMean environmental impact of each diet type：")
diet_stats = da.groupby('diet_group')[['mean_ghgs', 'mean_land', 'mean_watscar']].mean()
print(diet_stats)
print("-" * 80)

# Difference analysis between different age groups
print("\nDifferences in environmental impacts of different diet types within groups：")
for age_id in da['ID'].unique():
    print(f"\nAge Group {age_id}：")
    group_df = da[da['ID'] == age_id]
    print(group_df[['diet_group', 'mean_ghgs', 'mean_land', 'mean_watscar']].to_string(index=False))
    print("-" * 60)

# Print initial findings
print("\nResult:")

print(f"Age group with the greatest environmental impact：\n{age_stats.idxmax().to_string()}")
print(f"Diet type with the greatest environmental impact：\n{diet_stats.idxmax().to_string()}")

print("-" * 60)
print(f"Age group with the least environmental impact：\n{age_stats.idxmin().to_string()}")
print(f"Diet type with the least environmental impact：\n{diet_stats.idxmin().to_string()}")

