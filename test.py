import joblib
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

# Define Model Path
MODEL_PATH = 'models/savedmodel.joblib'  # use .joblib not .pth for joblib files

# Check if the model file exists
if not os.path.exists(MODEL_PATH):
    print(f"Error: Model file '{MODEL_PATH}' not found.")
    print("Please run train.py first to generate the model.")
    exit(1)

print("Loading test data...")
# Load the dataset
faces = fetch_olivetti_faces()
X, y = faces.data, faces.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, test_size=0.3, random_state=42, stratify=y
)
print("Test data loaded.")

# Load the saved model
print(f"Loading model from {MODEL_PATH} ...")
model = joblib.load(MODEL_PATH)
print("Model loaded.")

# Compute accuracy on the test set
print("Computing test accuracy...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Test Accuracy: {accuracy * 100:.2f}%")
