import pandas as pd
import numpy as np
import random

# Load IRIS dataset (without species column)
df = pd.read_csv("Datasets/Datasets/IRIS.csv")
data = df.drop("species", axis=1).values   # Only numeric columns

# Number of clusters
K = 3

# Randomly initialize cluster means (choose any 3 random points)
random_indices = random.sample(range(data.shape[0]), K)
means = data[random_indices]

print("Initial Cluster Means:")
for i, m in enumerate(means):
    print(f"Mean {i+1}: {m}")

# Function to compute Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# K-means iterations
for iteration in range(10):
    print(f"\nIteration {iteration+1}")

    # Step 1: Assign each point to nearest mean
    clusters = [[] for _ in range(K)]
    for point in data:
        distances = [euclidean_distance(point, mean) for mean in means]
        cluster_index = np.argmin(distances)
        clusters[cluster_index].append(point)

    # Step 2: Update means
    new_means = []
    for cluster in clusters:
        new_means.append(np.mean(cluster, axis=0))

    means = new_means

# Print final cluster means
print("\n==============================")
print("   FINAL CLUSTER MEANS (K=3)")
print("==============================")
for i, m in enumerate(means):
    print(f"Final Mean of Cluster {i+1}: {m}")
