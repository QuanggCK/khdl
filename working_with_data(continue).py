# Scatter plot

# Example: Load the studyhours dataset and plt to see the relationship between the study hours and scores

import pandas as pd
import matplotlib.pyplot as plt

#Load the gold price data from a CSV file
studyhours_df = pd.read_csv('../data/studyhours.csv')

#Display the first few rows of the DataFrame
print(studyhours_df.head())

#View the summary statistics of the DataFrame
print(studyhours_df.describe())

#Make a scatter plot of study hours vs. final grades
#Init figure with a specific size
plt.figure(figsize = (10,6))
#Get data values for study hours and exam scores
study_hours = studyhours_df['Study Hours']
exam_score = studyhours_df['Exam Score']
#Make a scatter plot of study hours vs. exam scores
plt.scatter(study_hours, exam_score, alpha=0.75, label="Cluster A")
plt.xlabel("Study hours")
plt.ylabel("Exam score")
plt.show()

# -------------------------------------------------------------------------------------------------------------------

# Example 2: Load the Iris dataset and make scatter plot
import pandas as pd
import matplotlib.pyplot as plt
# Import scikit-learn dataset module
import sklearn.datasets as datasets

# Load the Iris dataset from scikit-learning
iris = datasets.load_iris()

# Display statistics of the dataset
print("Iris dataset statistics:")
print(f"Number of samples: {iris.data.shape[0]}")
print(f"Number of features: {iris.data.shape[1]}")
print(f"Feature names: {iris.feature_names}")

# Make a scatter plot of sepal length vs. sepal width for the Iris dataset
# Init figure with a specific size

# Make a scatter plot of sepal length vs. sepal width for the Iris dataset
# Init figure with a specific size

plt.figure(figsize=(10, 6))
# Get data values for sepal length and sepal width
sepal_length = iris.data[:, 0]  # Sepal length is the first feature
sepal_width = iris.data[:, 1]   # Sepal width is the second feature
# print(f"Sepal length: {sepal_length[:5]}")  # Display first 5 values
# print(f"Sepal width: {sepal_width[:5]}")    # Display first
# Make a scatter plot of sepal length vs. sepal width for the Iris dataset

# Make label for each species in the Iris dataset
species = iris.target  # Species labels (0, 1, 2)
# Make a scatter plot of sepal length vs. sepal width for the Iris dataset, colored by species
plt.scatter(sepal_length, sepal_width, c=species, cmap='viridis',
            alpha=0.75,
            label="Sepal length vs Sepal width",
            )
plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width (cm)")
# Add a legend to the plot
plt.legend()
# Add legend  to indicate species
plt.show()

# Make a scatter plot of petal length vs. petal width for the Iris dataset
# Init figure with a specific size
plt.figure(figsize=(10, 6))
# Get data values for petal length and petal width
petal_length = iris.data[:, 2]  # Petal length is the third feature
petal_width = iris.data[:, 3]   # Petal width is the fourth feature
# Make label for each species in the Iris dataset
species = iris.target  # Species labels (0, 1, 2)
# Make a scatter plot of sepal length vs. sepal width for the Iris dataset, colored by species
plt.scatter(petal_length, petal_width, c=species, cmap='viridis',
            alpha=0.75,
            label="Petal length vs Petal width",
            )
plt.xlabel("Petal length (cm)")
plt.ylabel("Petal width (cm)")
# Add a legend to the plot
plt.legend()
# Add legend  to indicate species
plt.show()



