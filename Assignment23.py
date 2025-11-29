import pandas as pd
import math

# 1. Create the DataFrame from given data
data = {
    "Age": ["Young","young","Middle","Old","Old","Old","Middle","Young","Young","Old","Young","Middle","Middle","Old"],
    "Income": ["High","High","High","Medium","Low","Low","Low","Medium","Low","Medium","Medium","Medium","High","Medium"],
    "Married": ["Married","No","No","No","No","Yes","Yes","Yes","No","Yes","Yes","Yes","No","Yes"],
    "Health": ["Fair","Good","Fair","Fair","Fair","Good","Good","Fair","Fair","Fair","Good","Good","Fair","Good"],
    "Class": ["No","No","Yes","Yes","Yes","No","Yes","No","Yes","Yes","Yes","Yes","Yes","No"]
}

df = pd.DataFrame(data)

# Normalize Age values (capitalize)
df['Age'] = df['Age'].str.capitalize()

# 2. Frequency table for Age
freq_age = df['Age'].value_counts().rename_axis('Age').reset_index(name='Frequency')
freq_age['Proportion'] = freq_age['Frequency'] / len(df)
print("Frequency table for Age:\n", freq_age)

# 3. Define entropy function
def entropy(series):
    counts = series.value_counts()
    total = counts.sum()
    ent = 0.0
    for c in counts:
        p = c / total
        ent -= p * math.log2(p)
    return ent

# 4. Base entropy for Class
base_entropy = entropy(df['Class'])
print("\nBase Entropy (Class):", base_entropy)

# 5. Entropy by Age groups and weighted entropy
weighted_entropy = 0.0
for age_cat, subset in df.groupby('Age'):
    ent = entropy(subset['Class'])
    weight = len(subset) / len(df)
    weighted_entropy += weight * ent
    print(f"Age={age_cat}: count={len(subset)}, entropy={ent}, weight={weight}")

print("\nWeighted entropy after splitting on Age:", weighted_entropy)

# 6. Information Gain
info_gain = base_entropy - weighted_entropy
print("\nInformation Gain by splitting on Age:", info_gain)
