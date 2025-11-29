import math

# Points
points = {
    "P1": (0.1, 0.6),
    "P2": (0.15, 0.71),
    "P3": (0.08, 0.9),
    "P4": (0.16, 0.85),
    "P5": (0.2, 0.3),
    "P6": (0.25, 0.5),
    "P7": (0.24, 0.1),
    "P8": (0.3, 0.2)
}

# Initial centroids
m1 = points["P1"]   # (0.1, 0.6)
m2 = points["P8"]   # (0.3, 0.2)

# Function to compute distance
def dist(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

# Assign clusters
C1 = []
C2 = []

for pid, p in points.items():
    if dist(p, m1) < dist(p, m2):
        C1.append(pid)
    else:
        C2.append(pid)

print("Cluster 1 (C1):", C1)
print("Cluster 2 (C2):", C2)

# Updated centroids
def mean(points_list):
    x = sum(points[p][0] for p in points_list) / len(points_list)
    y = sum(points[p][1] for p in points_list) / len(points_list)
    return (x, y)

new_m1 = mean(C1)
new_m2 = mean(C2)

print("Updated m1:", new_m1)
print("Updated m2:", new_m2)
