import os
import joblib
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  # or your model

# Create models directory if not exists
os.makedirs('models', exist_ok=True)

# Load data and split (use same random_state/test_size as in test.py)
faces = fetch_olivetti_faces()
X, y = faces.data, faces.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, test_size=0.3, random_state=42, stratify=y
)

# Train your classifier (replace with your actual model)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model using joblib
joblib.dump(model, 'models/savedmodel.joblib')
print("Model saved to models/savedmodel.joblib")
