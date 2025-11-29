import pandas as pd

# Load iris dataset
df = pd.read_csv("Datasets/Datasets/IRIS.csv")

species_list = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

for sp in species_list:
    print(f"\n\n==============================")
    print(f"   Statistics for: {sp}")
    print("==============================")
    
    # Filter rows for each species
    data = df[df["species"] == sp]

    # BASIC STATISTICS
    print("\n--- Basic Statistics ---")
    print(data.describe())

    # PERCENTILES (only numeric columns)
    print("\n--- Percentiles (numeric only) ---")
    print(data.select_dtypes(include="number").quantile([0.25, 0.5, 0.75]))








