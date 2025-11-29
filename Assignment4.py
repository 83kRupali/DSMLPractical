import csv
import math

# Read CSV
data = []
with open("Datasets/Datasets/Lipstick.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

target = "Buys"
attributes = ["Age", "Income", "Gender", "Ms"]   # attributes to check

# Entropy function
def entropy(rows):
    total = len(rows)
    if total == 0: return 0
    yes = sum(1 for r in rows if r[target] == "Yes")
    no  = total - yes
    e = 0
    for count in (yes, no):
        if count != 0:
            p = count / total
            e -= p * math.log2(p)
    return e

# Information gain function
def info_gain(rows, attr):
    base = entropy(rows)
    values = {}
    for r in rows:
        values.setdefault(r[attr], []).append(r)
    weighted = sum((len(v)/len(rows)) * entropy(v) for v in values.values())
    return base - weighted

# Compute gain for all attributes
gains = {attr: info_gain(data, attr) for attr in attributes}

# Print and find root
for a, g in gains.items():
    print(a, "=>", round(g, 4))

root = max(gains, key=gains.get)
print("\nROOT NODE =", root)






