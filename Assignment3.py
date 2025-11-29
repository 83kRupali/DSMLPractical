import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Datasets/Datasets/House Data.csv")   # <-- Change filename if needed


# Select numeric columns only
numeric_cols = df.select_dtypes(include='number').columns

print("\n========== SUMMARY STATISTICS ==========\n")

# ---- COMPUTE STATISTIC FOR EACH FEATURE ----
for col in numeric_cols:
    print(f"\n--- {col.upper()} ---")
    
    # Standard Deviation
    print("Standard Deviation:")
    print(df[col].std())
    
    # Variance
    print("Variance:")
    print(df[col].var())
    
    # Percentiles
    print("Percentiles (25%, 50%, 75%):")
    print(df[col].quantile([0.25, 0.50, 0.75]))


# ---- HISTOGRAMS FOR EACH NUMERIC FEATURE ----
print("\n\n========== GENERATING HISTOGRAMS ==========\n")

for col in numeric_cols:
    plt.figure(figsize=(7, 4))
    plt.hist(df[col].dropna(), bins=30)     # dropna fixes empty graphs
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
