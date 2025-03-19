import pandas as pd
import seaborn as sns #Advanced Visualization Libraries
import matplotlib.pyplot as plt #Drawing Library

# Reading Data Files
data = pd.read_csv("3 Data Aggregation.csv")

# Convert age groups (ID) to text labels for easier visualization and data analysis
age_labels = {1: "20-29", 2: "30-39", 3: "40-49", 4: "50+"}
data["age_groups"] = data["ID"].map(age_labels)

# Unified order of food types
diet_order = ['vegan', 'veggie', 'fish', 'meat', 'meat50', 'meat100']

# Pivot table function to define heatmap
def create_table(df, value):
    pivot_df = df.pivot(index='age_groups', columns='diet_group', values=value)
    pivot_df = pivot_df[diet_order]
    return pivot_df

# Set the drawing style: color and font size
sns.set_theme(style="whitegrid", font_scale=1.8)

# Heatmap 1: mean_ghgs
plt.figure(figsize=(12, 8))
sns.heatmap(create_table(data, 'mean_ghgs'), annot=True, cmap=["#ffccff", "#ff99ff", "#ff66ff", "#ff33ff", "#cc00cc", "#800080"], fmt=".3f")
plt.title("Heatmap of gas emissions by age group and diet type")
plt.xlabel("Diet Type (Chart 1)")
plt.ylabel("Age Group")
plt.tight_layout()
plt.show()

# Heatmap 2: mean_land
plt.figure(figsize=(12, 8))
sns.heatmap(create_table(data, 'mean_land'), annot=True, cmap=["#b3ffe0", "#80ffbf", "#4dff99", "#1aff66", "#00994d", "#004d26"], fmt=".3f")
plt.title("Heatmap of agricultural land use by age group and diet type")
plt.xlabel("Diet Type (Chart 2)")
plt.ylabel("Age Group")
plt.tight_layout()
plt.show()

# Heatmap 2: mean_watscar
plt.figure(figsize=(12, 8))
sns.heatmap(create_table(data, 'mean_watscar'), annot=True, cmap=["#99e6ff", "#66ccff", "#33b5e5", "#0099cc", "#007399", "#005266"], fmt=".0f")
plt.title("Heatmap of water stress by age group and diet type")
plt.xlabel("Diet Type (Chart 3)")
plt.ylabel("Age Group")
plt.tight_layout()
plt.show()
