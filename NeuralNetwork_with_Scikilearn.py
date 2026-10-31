from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# Load the digits dataset
X_d, y_d = load_digits(return_X_y=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_d, y_d, test_size=0.2, random_state=42)

# Create a pipepline with a StandardScaler and a MLPClassifier
mlp = make_pipeline(StandardScaler(),
MLPClassifier(hidden_layer_sizes=(100,),
max_iter=500, random_state=42))

# Train the model
mlp.fit(X_train, y_train)

# Evaluate the model on the test set
accuracy = mlp.score(X_test, y_test)
print(f"Test set accuracy: {100*accuracy:.2f}%")