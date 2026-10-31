# Unsupervised Learning
# Clutering

# Import iris dataset
from sklearn.datasets import load_iris
# import k-Means clustering model
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target
print(y)

# Set k = 3 and fit the model

km = KMeans(n_clusters = 3,
init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = km.fit_predict(X)
# Get the cluster labels
labels = km.labels_
# Evaluate the model using the silhouette score
silhouette_avg = silhouette_score(X, labels)
print("For n_clusters =", 3,
      "The average silhouette_score is :", silhouette_avg)

from sklearn.metrics import accuracy_score
import numpy as np
from scipy.stats import mode

# Because K-means labels are arbitrary, we match each cluster to the most frequent true label in it.
predicted_labels = np.zeros_like(labels)
for i in range(3):
    mask = (labels == i)
    if np.any(mask):
        # Find the most common true label in this specific cluster
        true_mode, _ = mode(y[mask], keepdims=True)
        predicted_labels[mask] = true_mode[0]

# 4. Calculate the classification accuracy
accuracy = accuracy_score(y, predicted_labels)
print(f"K-means Accuracy: {accuracy * 100:.2f}%")