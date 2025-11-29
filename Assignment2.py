import pandas as pd

# Load dataset
df = pd.read_csv("Datasets/Datasets/Telecom_Churn.csv")

# Numeric columns only
num_cols = df.select_dtypes(include=['number']).columns

print("\n========== SUMMARY STATISTICS FOR TELECOM CHURN DATASET ==========\n")

for col in num_cols:
    print(f"\n------ {col.upper()} ------")

    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())
    print("Mean:", df[col].mean())
    print("Range:", df[col].max() - df[col].min())
    print("Standard Deviation:", df[col].std())
    print("Variance:", df[col].var())
    print("Percentiles:")
    print(df[col].quantile([0.25, 0.50, 0.75]))
