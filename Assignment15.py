import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load titanic dataset
df = pd.read_csv("Datasets/Datasets/Titanic.csv")   # your local file
# If seaborn dataset needed:  df = sns.load_dataset("titanic")

print(df.head())

# ------------------------------
# 1. Survival count
# ------------------------------
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.show()

# ------------------------------
# 2. Survival by Gender
# ------------------------------
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.show()

# ------------------------------
# 3. Survival by Passenger Class
# ------------------------------
sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Survival by Passenger Class")
plt.show()

# ------------------------------
# 4. Age Distribution
# ------------------------------
sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution of Passengers")
plt.show()

# ------------------------------
# 5. Fare vs Pclass
# ------------------------------
sns.boxplot(x="Pclass", y="Fare", data=df)
plt.title("Fare Distribution by Class")
plt.show()

# ------------------------------
# 6. Heatmap for Correlation
# ------------------------------
numeric_df = df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]]
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
