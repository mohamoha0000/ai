import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler

# 1. Generate and scale data
X = np.array([i for i in range(1, 11)], dtype=np.float32).reshape(-1, 1)  # Numbers 1 to 100
y = np.array([1 if i % 2 != 0 else 0 for i in range(1, 11)], dtype=np.float32)  # Labels: 0 for even, 1 for odd

# Scale X to the range [0, 1]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 2. Define a simpler model
model = tf.keras.Sequential([
    layers.Dense(8, activation='relu', input_shape=(1,)),  # Simpler layer with 8 neurons
    layers.Dense(8, activation='relu'),  # One more hidden layer
    layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# 3. Compile the model with a smaller learning rate
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 4. Train the model with more epochs and batch size
history = model.fit(X_scaled, y, epochs=500, batch_size=5, verbose=1)

# 5. Evaluate the model
loss, accuracy = model.evaluate(X_scaled, y, verbose=0)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# 6. Make predictions and debug
predictions = model.predict(X_scaled)
predicted_classes = (predictions > 0.5).astype(int)

# Display predictions and expected results for debugging
for i in range(1, 101):
    print(f"Number {i} - Predicted: {'Odd' if predicted_classes[i-1] == 1 else 'Even'}; Actual: {'Odd' if y[i-1] == 1 else 'Even'}")
