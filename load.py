
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler

X = np.array([i for i in range(1, 101)], dtype=np.float32).reshape(-1, 1)
y = np.array([1 if i % 2 != 0 else 0 for i in range(1, 101)], dtype=np.float32)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
loaded_model = tf.keras.models.load_model('even_odd_classifier_model.h5')
print("Model loaded successfully.")

# You can now use the loaded model to make predictions or evaluate it
loaded_predictions = loaded_model.predict(X_scaled)
loaded_predicted_classes = (loaded_predictions > 0.5).astype(int)

# Display loaded model's predictions for verification
for i in range(1, 10):
    print(f"Number {i} - Loaded Model Prediction: {'Odd' if loaded_predicted_classes[i-1] == 1 else 'Even'}; Actual: {'Odd' if y[i-1] == 1 else 'Even'}")
