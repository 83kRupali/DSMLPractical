import pandas as pd

# -----------------------------
# 1. Load the dataset
# -----------------------------
df = pd.read_csv("Datasets/Datasets/Lung Cancer.csv")

print("\n=== Original Dataset ===")
print(df)

# -----------------------------
# 2. Check if data is clean
# -----------------------------
print("\n=== Checking for Null Values ===")
print(df.isnull().sum())

print("\n=== Checking Data Types ===")
print(df.dtypes)

print("\n=== Checking for Duplicates ===")
print(df.duplicated().sum())

# -----------------------------
# 3. Data Cleaning
# -----------------------------

# 3A. Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())   # numerical
df["Smokes"] = df["Smokes"].fillna("Unknown")    # categorical
df["AreaQ"] = df["AreaQ"].fillna("Unknown")
df["Alkhol"] = df["Alkhol"].fillna("Unknown")
df["Result"] = df["Result"].fillna("Pending")

# 3B. Remove duplicate rows
df = df.drop_duplicates()

# 3C. Fix data types if needed
df["Age"] = df["Age"].astype(int)

# -----------------------------
# 4. Data Transformation
# -----------------------------

# 4A. Create a new column: Age Group
df["Age_Group"] = pd.cut(df["Age"],
                         bins=[0, 18, 40, 60, 100],
                         labels=["Teen", "Adult", "Middle", "Senior"])

# 4B. Convert categorical columns to uppercase
df["Name"] = df["Name"].str.upper()
df["Surname"] = df["Surname"].str.upper()

# 4C. Encode Smokes column (Yes=1, No=0, Unknown=-1)
df["Smokes_Code"] = df["Smokes"].map({"Yes": 1, "No": 0, "Unknown": -1})

# -----------------------------
# 5. Final Cleaned Dataset
# -----------------------------
print("\n=== Cleaned & Transformed Dataset ===")
print(df)

# -----------------------------
# 6. Save cleaned data
# -----------------------------
df.to_csv("cleaned_dataset.csv", index=False)
