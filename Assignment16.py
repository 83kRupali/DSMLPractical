import seaborn as sns
import matplotlib.pyplot as plt

# Load the inbuilt Titanic dataset
titanic = sns.load_dataset("Datasets/Datasets/titanic")

# Plot histogram of ticket fare
plt.figure(figsize=(8,5))
sns.histplot(titanic["fare"], kde=True)
plt.title("Distribution of Passenger Ticket Fare")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()
