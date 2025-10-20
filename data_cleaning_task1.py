import pandas as pd
import numpy as np

# Step 2: Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Step 3: Display basic info
print("Dataset shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nFirst 5 rows:\n", df.head())

# Step 4: Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Fill missing values (if any)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Annual Income (k$)'].fillna(df['Annual Income (k$)'].mean(), inplace=True)
df['Spending Score (1-100)'].fillna(df['Spending Score (1-100)'].mean(), inplace=True)

# Step 5: Remove duplicates
before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]
print(f"\nRemoved {before - after} duplicate rows.")

# Step 6: Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')
print("\nCleaned column names:", df.columns)

# Step 7: Standardize text values (Gender column)
df['gender'] = df['gender'].str.strip().str.lower()
df['gender'] = df['gender'].replace({'male': 'Male', 'm': 'Male', 'female': 'Female', 'f': 'Female'})

# Step 8: Check and fix data types
df['age'] = df['age'].astype(int)
df['annual_income_(k$)'] = df['annual_income_(k$)'].astype(float)
df['spending_score_(1-100)'] = df['spending_score_(1-100)'].astype(int)

# Step 9: Verify cleaned data
print("\nCleaned Data Overview:")
print(df.info())
print(df.head())

# Step 10: Save cleaned dataset
df.to_csv("cleaned_mall_customers.csv", index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_mall_customers.csv'")
