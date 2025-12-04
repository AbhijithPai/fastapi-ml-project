import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")
