# Customer Shopping Data Cleaning & Analysis
# ------------------------------------------------
# Project: Data Cleaning using Python, Pandas and NumPy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv("customer_shopping_dirty_data.csv")

# 2. Inspect data
print(df.head())
print(df.info())
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# 3. Clean text columns
df["Name"] = df["Name"].astype("string").str.strip().str.replace(r"\s+", " ", regex=True)
df["City"] = df["City"].astype("string").str.strip()
df["Gender"] = df["Gender"].replace({"M": "Male", "F": "Female"}).astype("string").str.strip()

# 4. Clean Age
df["Age"] = df["Age"].astype("string").str.strip().replace({"thirty": "30"})
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df.loc[~df["Age"].between(18, 100), "Age"] = np.nan
df["Age"] = df["Age"].fillna(df["Age"].median()).round().astype(int)

# 5. Validate email addresses
email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
df["Email"] = df["Email"].astype("string").str.strip()
df.loc[~df["Email"].str.match(email_pattern, na=False), "Email"] = pd.NA

# 6. Clean purchase amount
df["Purchase_Amount"] = pd.to_numeric(df["Purchase_Amount"], errors="coerce")
df.loc[df["Purchase_Amount"] < 0, "Purchase_Amount"] = np.nan
df["Purchase_Amount"] = df["Purchase_Amount"].fillna(df["Purchase_Amount"].median())

# 7. Standardize dates
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"], errors="coerce")
df["Purchase_Date"] = df["Purchase_Date"].fillna(df["Purchase_Date"].median())

# 8. Clean ratings
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df.loc[~df["Rating"].between(1, 5), "Rating"] = np.nan
df["Rating"] = df["Rating"].fillna(df["Rating"].median())

# 9. Remove exact duplicate rows
df = df.drop_duplicates()

# 10. Basic analysis
print("\nTotal customers:", df["Customer_ID"].nunique())
print("Total purchase amount:", df["Purchase_Amount"].sum())
print("Average purchase amount:", df["Purchase_Amount"].mean())
print("Average rating:", df["Rating"].mean())

print("\nSales by city:")
print(df.groupby("City")["Purchase_Amount"].sum().sort_values(ascending=False))

print("\nAverage rating by gender:")
print(df.groupby("Gender")["Rating"].mean())

# 11. Visualizations
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="City", y="Purchase_Amount", estimator="sum", errorbar=None)
plt.title("Total Purchase Amount by City")
plt.xlabel("City")
plt.ylabel("Total Purchase Amount")
plt.tight_layout()
plt.savefig("sales_by_city.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=8, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("age_distribution.png")
plt.show()

# 12. Save cleaned data
df.to_csv("customer_shopping_cleaned.csv", index=False)
print("\nCleaned dataset saved successfully.")
