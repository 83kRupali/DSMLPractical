import math

# All points
points = {
    "P1": (2, 10),
    "P2": (2, 5),
    "P3": (8, 4),
    "P4": (5, 8),
    "P5": (7, 5),
    "P6": (6, 4),
    "P7": (1, 2),
    "P8": (4, 9)
}

# Initial centroids
m1 = points["P1"]   # (2,10)
m2 = points["P4"]   # (5,8)
m3 = points["P7"]   # (1,2)

# Function to compute Euclidean distance
def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# Assign points to clusters
C1, C2, C3 = [], [], []

for pid, p in points.items():
    d1 = dist(p, m1)
    d2 = dist(p, m2)
    d3 = dist(p, m3)

    mn = min(d1, d2, d3)

    if mn == d1:
        C1.append(pid)
    elif mn == d2:
        C2.append(pid)
    else:
        C3.append(pid)

print("Cluster 1:", C1)
print("Cluster 2:", C2)
print("Cluster 3:", C3)

# Function to calculate centroid
def centroid(cluster):
    x = sum(points[p][0] for p in cluster) / len(cluster)
    y = sum(points[p][1] for p in cluster) / len(cluster)
    return (x, y)

# Updated centroids
new_m1 = centroid(C1)
new_m2 = centroid(C2)
new_m3 = centroid(C3)

print("\nUpdated m1:", new_m1)
print("Updated m2:", new_m2)
print("Updated m3:", new_m3)




# 1) Which cluster does P6 belong to?
# ans - P6 belongs to Cluster C2


# 2) What is the population of cluster around m3?
# ans - m3 cluster = C3 = { P7 }
# Population = 1


# 3) 






# incompleted



