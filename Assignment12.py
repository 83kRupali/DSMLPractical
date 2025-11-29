import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# Load the Iris dataset (CSV file)
# --------------------------------------------------
df = pd.read_csv("Datasets/Datasets/IRIS.csv")

# --------------------------------------------------
# 1. Create box plots for each numerical feature
# --------------------------------------------------
numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

df[numeric_cols].plot(kind="box", subplots=True, layout=(2,2), figsize=(10,8), title="Iris Dataset Boxplots")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 2. Identify outliers using the IQR method
# --------------------------------------------------
print("\n--- Outlier Detection (IQR Method) ---\n")

for col in numeric_cols:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]

    print(f"{col}:")
    print(f"  Lower Bound = {lower_bound:.2f}, Upper Bound = {upper_bound:.2f}")

    if len(outliers) > 0:
        print("  Outliers found:", list(outliers))
    else:
        print("  No outliers found.")

    print()
