# import pandas as pd
# import numpy as np
# import random

# # Load Iris dataset
# df = pd.read_csv("Datasets/Datasets/IRIS.csv")

# # Use only numeric columns (drop species)
# data = df.drop("species", axis=1).values

# # Number of clusters
# K = 4


# # Random initialization of K means
# random_indices = random.sample(range(data.shape[0]), K)
# means = data[random_indices]

# print("Initial Cluster Means:")
# for i, m in enumerate(means):
#     print(f"Mean {i+1}: {m}")

# # Function to compute Euclidean distance
# def euclidean_distance(a, b):
#     return np.sqrt(np.sum((a - b) ** 2))

# # Perform 10 iterations of K-means
# for iteration in range(10):
#     print(f"\nIteration {iteration+1}")

#     # Step 1: Assign points to nearest centroid
#     clusters = [[] for _ in range(K)]
    
#     for point in data:
#         distances = [euclidean_distance(point, mean) for mean in means]
#         cluster_index = np.argmin(distances)
#         clusters[cluster_index].append(point)

#     # Step 2: Update means
#     new_means = []
#     for cluster in clusters:
#         if len(cluster) > 0:
#             new_means.append(np.mean(cluster, axis=0))
#         else:  # If a cluster becomes empty, choose a random point
#             new_means.append(data[random.randint(0, data.shape[0] - 1)])

#     means = new_means

# # Print the final cluster means
# print("\n==============================")
# print("   FINAL CLUSTER MEANS (K=4)")
# print("==============================")

# for i, m in enumerate(means):
#     print(f"Final Mean of Cluster {i+1}: {m}")





import pandas as pd
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Datasets/Datasets/IRIS.csv")

# Use only numeric columns (first 4)
X = df.iloc[:, :4]

# KMeans model with K = 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)

# Fit the model
kmeans.fit(X)

# Print final cluster centers
print("Final Cluster Means (K = 3):")
print(kmeans.cluster_centers_)



