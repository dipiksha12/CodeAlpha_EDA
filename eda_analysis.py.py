import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books.csv")

# Display first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Plot Ratings Count
df["Rating"].value_counts().plot(kind="bar")
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()