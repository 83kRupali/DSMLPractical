import pandas as pd

# Load dataset (make sure the file is in the same folder as this .py file)
df = pd.read_csv("Datasets/Datasets/covid_vaccine_statewise.csv")

# CLEAN COLUMN NAMES (important!)
df.columns = df.columns.str.strip()

# A. Describe the dataset
print("\n--- Dataset Description ---")
print(df.describe(include='all'))

# Check actual column names
print("\n--- Column Names ---")
print(df.columns)

# B. Number of males vaccinated
if "Male (Doses Administered)" in df.columns:
    total_males = df["Male (Doses Administered)"].sum()
    print("\nTotal Males Vaccinated:", total_males)
else:
    print("\n'Male (Doses Administered)' column not found!")

# C. Number of females vaccinated
if "Female (Doses Administered)" in df.columns:
    total_females = df["Female (Doses Administered)"].sum()
    print("Total Females Vaccinated:", total_females)
else:
    print("'Female (Doses Administered)' column not found!")
