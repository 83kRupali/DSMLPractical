import pandas as pd

# Load dataset
df = pd.read_csv("Datasets/Datasets/House Data.csv")

# Display first few rows
print("\n--- Dataset Preview ---")
print(df.head())

# Identify categorical and quantitative columns
categorical_cols = df.select_dtypes(include=['object']).columns
quantitative_cols = df.select_dtypes(include=['int64', 'float64']).columns

print("\nCategorical Variables:", list(categorical_cols))
print("Quantitative Variables:", list(quantitative_cols))

# -------------------------------------------------------
# Summary statistics for each quantitative variable grouped by each categorical variable
# -------------------------------------------------------
for cat in categorical_cols:
    print(f"\n\n============================")
    print(f" Summary Statistics Grouped by: {cat}")
    print(f"============================")

    for num in quantitative_cols:
        print(f"\n--- {num} grouped by {cat} ---")
        summary = df.groupby(cat)[num].agg(['mean', 'median', 'min', 'max', 'std'])
        print(summary)






