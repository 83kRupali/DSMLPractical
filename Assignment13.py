import pandas as pd

# Load CSV
df = pd.read_csv("Datasets/Datasets/covid_vaccine_statewise.csv")

# # CLEAN COLUMN NAMES
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("/", "_")

# # SHOW CLEANED COLUMNS
print("Cleaned columns:")
print(df.columns)

# # DROP duplicates and NA states
df = df.dropna(subset=["State"]).drop_duplicates()

# # Convert numeric columns to numeric
num_cols = df.select_dtypes(include='object').columns
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='ignore')

# ----------- (a) Describe dataset -------------
print("\nDataset Description:")
print(df.describe(include='all'))

# ----------- (b) First Dose per State -------------
print("\nState-wise First Dose Administered:")
if "First_Dose_Administered" in df.columns:
    first_dose = df.groupby("State")["First_Dose_Administered"].sum()
    print(first_dose)
else:
    print("Column name mismatch for First Dose.")

# ----------- (c) Second Dose per State -------------
print("\nState-wise Second Dose Administered:")
if "Second_Dose_Administered" in df.columns:
    second_dose = df.groupby("State")["Second_Dose_Administered"].sum()
    print(second_dose)
else:
    print("Column name mismatch for Second Dose.")
