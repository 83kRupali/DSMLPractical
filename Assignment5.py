import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# -------------------------------
# 1. Load the dataset
# -------------------------------
df = pd.read_csv("Datasets/Datasets/Lipstick.csv")

# -------------------------------
# 2. Separate features and target
# -------------------------------
X = df.drop(["Id","Buys"], axis=1)
y = df["Buys"]

# -------------------------------
# 3. Encode categorical columns
# -------------------------------
encoders = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

# -------------------------------
# 4. Train Decision Tree
# -------------------------------
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

# -------------------------------
# 5. Test Input
# -------------------------------
test = pd.DataFrame({
    "Age":["21-35"],
    "Income":["Low"],
    "Gender":["Female"],
    "Ms":["Married"]
})

# encode test row
for col in test.columns:
    test[col] = encoders[col].transform(test[col])

# -------------------------------
# 6. Predict
# -------------------------------
pred = model.predict(test)[0]
result = target_encoder.inverse_transform([pred])[0]

print("Prediction for test data:", result)
