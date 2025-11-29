import pandas as pd

# ------------------------------
# 1. Create a sample dataset
# ------------------------------
data = {
    "ID": [1, 2, 3, 4, 5],
    "Age": [25, 30, None, 40, 35],
    "Income": ["50000", "60000", "55000", None, "70000"],
    "Gender": ["Male", "Female", "Male", "Female", None]
}

df = pd.DataFrame(data)

print("\n--- Original Dataset ---")
print(df)


# ------------------------------
# 2. Counting unique values
# ------------------------------
print("\n--- Unique Value Counts ---")
print(df.nunique())


# ------------------------------
# 3. Check column formats (data types)
# ------------------------------
print("\n--- Data Types Before Conversion ---")
print(df.dtypes)


# ------------------------------
# 4. Converting variable data types
# ------------------------------

# Convert Income column from string to integer
df["Income"] = pd.to_numeric(df["Income"], errors="coerce")

# Convert ID from int64 to int16 (short)
df["ID"] = df["ID"].astype("int16")

print("\n--- Data Types After Conversion ---")
print(df.dtypes)


# ------------------------------
# 5. Identifying missing values
# ------------------------------
print("\n--- Missing Values in Each Column ---")
print(df.isnull().sum())


# ------------------------------
# 6. Filling missing values
# ------------------------------
df["Age"] = df["Age"].fillna(df["Age"].mean())      # Fill Age with mean
df["Income"] = df["Income"].fillna(df["Income"].median())  # Fill Income with median
df["Gender"] = df["Gender"].fillna("Unknown")       # Fill Gender with a category

print("\n--- Dataset After Filling Missing Values ---")
print(df)
