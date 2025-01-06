# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = r"/Users/alyaantharwani/Downloads/archive/2023-2024 NBA Player Stats - Regular.csv"  # Replace with your actual file path
data = pd.read_csv(file_path, encoding='ISO-8859-1', sep=';')

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Summary of the dataset (column names, data types, missing values)
print("\nData Info:")
print(data.info())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Descriptive statistics for numerical columns
print("\nDescriptive Statistics:")
print(data.describe())

# Exploratory Data Analysis (EDA)

# 1. Top 10 players by points per game (PPG)
top_10_ppg = data[['Player', 'PTS']].sort_values(by='PTS', ascending=False).head(10)
print("\nTop 10 Players by Points per Game:")
print(top_10_ppg)

# 2. Top 10 players by assists per game (APG)
top_10_apg = data[['Player', 'AST']].sort_values(by='AST', ascending=False).head(10)
print("\nTop 10 Players by Assists per Game:")
print(top_10_apg)

# 3. Top 10 players by rebounds per game (RPG)
top_10_rpg = data[['Player', 'TRB']].sort_values(by='TRB', ascending=False).head(10)
print("\nTop 10 Players by Rebounds per Game:")
print(top_10_rpg)

# 4. Top 10 players by field goal percentage (FG%)
top_10_fg = data[['Player', 'FG%']].sort_values(by='FG%', ascending=False).head(10)
print("\nTop 10 Players by Field Goal Percentage:")
print(top_10_fg)

# Data Visualization

# 1. Points per Game Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['PTS'], kde=True, bins=30, color='blue')
plt.title('Distribution of Points per Game (PPG)')
plt.xlabel('Points per Game')
plt.ylabel('Frequency')
plt.show()

# 2. Correlation Heatmap
# Calculate the correlation matrix, only with numeric columns
correlation_matrix = data.select_dtypes(include=['float64', 'int64']).corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of NBA Player Statistics')
plt.show()

# 3. Points vs Assists
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PTS', y='AST', data=data, color='green')
plt.title('Points vs Assists')
plt.xlabel('Points per Game (PTS)')
plt.ylabel('Assists per Game (AST)')
plt.show()

# 4. Top 10 players by Points, Rebounds, and Assists
top_10_stats = data[['Player', 'PTS', 'TRB', 'AST']].sort_values(by='PTS', ascending=False).head(10)

# Plot
top_10_stats.set_index('Player').plot(kind='bar', figsize=(12, 8))
plt.title('Top 10 Players by Points, Rebounds, and Assists')
plt.xlabel('Player')
plt.ylabel('Stats')
plt.show()

# Optional: Save cleaned data to a new CSV file
# data_cleaned = data.dropna()  # Example: remove rows with missing values
# data_cleaned.to_csv('NBA_Player_Stats_Cleaned.csv', index=False)
