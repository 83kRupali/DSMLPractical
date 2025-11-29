import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------
# 1. Load Iris dataset from CSV
# -----------------------------------------
df = pd.read_csv("Datasets/Datasets/IRIS.csv")

# -----------------------------------------
# 2. List features and their types
# -----------------------------------------
print("\nFeatures and their types:\n")
for col in df.columns:
    if df[col].dtype == 'object':
        dtype = "Nominal (Categorical)"
    else:
        dtype = "Numeric"
    print(f"{col}  -->  {dtype}")

# -----------------------------------------
# 3. Create histograms for numeric features
# -----------------------------------------
numeric_features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

df[numeric_features].hist(figsize=(10, 8))
plt.suptitle("Histograms of Iris Features", fontsize=15)
plt.show()
