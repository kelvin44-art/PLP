# Iris Dataset Analysis
# Author: Chris Thompson
# Date: May 12, 2025

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set the style for our plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")

print("Starting analysis of the Iris dataset...")

# Task 1: Load and Explore the Dataset
print("\n--- TASK 1: LOADING AND EXPLORING THE DATASET ---\n")

# Load the Iris dataset from sklearn
print("Loading the Iris dataset...")
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(data.head())

# Check the structure of the dataset
print("\nDataset info:")
print(data.info())

# Check for missing values
print("\nChecking for missing values:")
print(data.isnull().sum())

# No missing values to clean, so we're good to go!
print("\nNo missing values found. Dataset is clean.")

# Task 2: Basic Data Analysis
print("\n--- TASK 2: BASIC DATA ANALYSIS ---\n")

# Computing basic statistics
print("Basic statistics for the dataset:")
print(data.describe())

# Perform grouping by species
print("\nGrouping data by species:")
grouped_data = data.groupby('species').mean()
print(grouped_data)

# Add some observations
print("\nInteresting findings:")
print("- Setosa has the smallest petal dimensions but larger sepal width")
print("- Virginica has the largest petal dimensions overall")
print("- There seems to be a clear distinction between species based on these measurements")

# Task 3: Data Visualization
print("\n--- TASK 3: DATA VISUALIZATION ---\n")

# Let's create a figure with subplots for our visualizations
plt.figure(figsize=(16, 12))

# 1. Line chart - simulating a time series
# For demonstration, let's simulate monthly measurements
print("Creating line chart (simulated time series)...")
plt.subplot(2, 2, 1)

# Creating simulated monthly data
np.random.seed(42)  # For reproducibility
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
setosa_data = [4.5 + np.random.randn() * 0.3 for _ in range(12)]
versicolor_data = [5.7 + np.random.randn() * 0.4 for _ in range(12)]
virginica_data = [6.5 + np.random.randn() * 0.3 for _ in range(12)]

# Plotting
plt.plot(months, setosa_data, marker='o', label='Setosa')
plt.plot(months, versicolor_data, marker='s', label='Versicolor')
plt.plot(months, virginica_data, marker='^', label='Virginica')
plt.xlabel('Month')
plt.ylabel('Average Sepal Length (cm)')
plt.title('Monthly Trend of Sepal Length (Simulated)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# 2. Bar chart - comparison across categories
print("Creating bar chart...")
plt.subplot(2, 2, 2)

# Setting up data for the bar chart
species = grouped_data.index
x = np.arange(len(species))
width = 0.2

# Creating bars
plt.bar(x - width*1.5, grouped_data['sepal length (cm)'], width, label='Sepal Length')
plt.bar(x - width/2, grouped_data['sepal width (cm)'], width, label='Sepal Width')
plt.bar(x + width/2, grouped_data['petal length (cm)'], width, label='Petal Length')
plt.bar(x + width*1.5, grouped_data['petal width (cm)'], width, label='Petal Width')

# Adding labels and title
plt.xlabel('Species')
plt.ylabel('Average Value (cm)')
plt.title('Average Measurements by Species')
plt.xticks(x, species)
plt.legend()
plt.tight_layout()

# 3. Histogram - distribution of a numerical column
print("Creating histogram...")
plt.subplot(2, 2, 3)

# Creating histogram for petal length with colored bins by species
for species_name in iris.target_names:
    plt.hist(data[data['species'] == species_name]['petal length (cm)'], 
             alpha=0.5, bins=10, label=species_name)

plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Petal Length by Species')
plt.legend()
plt.tight_layout()

# 4. Scatter plot - relationship between two numerical columns
print("Creating scatter plot...")
plt.subplot(2, 2, 4)

# Creating scatter plot with colors by species
for i, species_name in enumerate(iris.target_names):
    species_data = data[data['species'] == species_name]
    plt.scatter(species_data['sepal length (cm)'], 
                species_data['petal length (cm)'], 
                label=species_name)

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Sepal Length vs Petal Length')
plt.legend()
plt.tight_layout()

# Save the figure
plt.savefig('iris_visualizations.png', dpi=300, bbox_inches='tight')
print("Saved visualizations to 'iris_visualizations.png'")

# Additional analysis: correlation matrix
print("\nCreating correlation matrix...")
plt.figure(figsize=(10, 8))
numeric_data = data.select_dtypes(include=[np.number])
correlation = numeric_data.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('iris_correlation.png', dpi=300)
print("Saved correlation matrix to 'iris_correlation.png'")

# Summary of findings
print("\n--- SUMMARY OF FINDINGS ---\n")
print("1. The Iris dataset consists of 150 samples with 4 numerical features and no missing values.")
print("2. The three species (Setosa, Versicolor, and Virginica) show distinct characteristics:")
print("   - Setosa has smaller petals but wider sepals")
print("   - Virginica has the largest measurements overall")
print("   - Versicolor falls in between the other two species")
print("3. Petal dimensions show more variation between species than sepal dimensions.")
print("4. The scatter plot reveals a strong correlation between sepal length and petal length.")
print("5. The histogram shows a clear bimodal distribution in petal length, indicating natural separation between species.")
print("6. The correlation matrix shows strong relationships between several measurements, particularly petal dimensions.")
print("\nThis analysis demonstrates that the Iris dataset is well-suited for classification tasks due to the clear differences between species.")

print("\nAnalysis completed successfully!")