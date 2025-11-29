# Given values
TP = 1
FP = 1
FN = 8
TN = 90

# Total samples
total = TP + FP + FN + TN

# Calculating metrics
accuracy = (TP + TN) / total
error_rate = (FP + FN) / total
precision = TP / (TP + FP)
recall = TP / (TP + FN)

# Display the results
print("Accuracy:", accuracy)
print("Error Rate:", error_rate)
print("Precision:", precision)
print("Recall:", recall)




