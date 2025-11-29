# ---------------------------------------------------------
# 1. Import Required Libraries
# ---------------------------------------------------------
import pandas as pd

# ---------------------------------------------------------
# 2. Read Data from Different Formats (CSV and Excel)
# ---------------------------------------------------------

# Read from CSV file
df_csv = pd.read_csv("Datasets/Datasets/Titanic.csv")        # <-- use your Titanic file


print("----- DATA FROM CSV FILE -----")
print(df_csv.head(), "\n")


# ---------------------------------------------------------
# 3. Indexing and Selecting Data
# ---------------------------------------------------------

# Selecting first 5 rows
print("----- FIRST 5 ROWS -----")
print(df_csv.head(), "\n")

# Selecting specific columns from Titanic dataset
print("----- SELECTING 'Name', 'Sex', 'Age' COLUMNS -----")
print(df_csv[['Name', 'Sex', 'Age']].head(), "\n")

# Selecting rows by index location
print("----- ROWS 10 TO 20 -----")
print(df_csv.iloc[10:21], "\n")


# ---------------------------------------------------------
# 4. Sorting the Data
# ---------------------------------------------------------

# Sort passengers by Age
print("----- SORTED BY AGE -----")
print(df_csv.sort_values(by="Age").head(), "\n")

# Sort by Fare (highest first)
print("----- SORTED BY FARE (DESCENDING) -----")
print(df_csv.sort_values(by="Fare", ascending=False).head(), "\n")


# ---------------------------------------------------------
# 5. Describe Attributes of the Data
# ---------------------------------------------------------

print("----- DESCRIPTIVE STATISTICS -----")
print(df_csv.describe(include='all'), "\n")


# ---------------------------------------------------------
# 6. Checking Data Types of Each Column
# ---------------------------------------------------------

print("----- DATA TYPES OF COLUMNS -----")
#print(df_csv['Age'].dtypes)
print(df_csv.dtypes)