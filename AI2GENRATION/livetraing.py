import numpy as np
import matplotlib.pyplot as plt

# Input data (features) and output (targets) for a linear relationship
X = np.array([[1], [2], [3], [4], [5], [6], [7]], dtype=np.float32)
y = np.array([[2], [4], [6], [8], [10], [12], [14]], dtype=np.float32)

# Scale data to improve network training stability
X_scaled = X / 100.0
y_scaled = y / 100.0

# Neural network hyperparameters
input_size = 1
hidden_size = 1
output_size = 1
learning_rate = 0.01
epochs = 100000

# Initialize weights and biases
np.random.seed(1)
weights_input_hidden = np.random.rand(input_size, hidden_size)
weights_hidden_output = np.random.rand(hidden_size, output_size)
bias_hidden = np.random.rand(1, hidden_size)
bias_output = np.random.rand(1, output_size)

# Set up the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
ax.plot(X, y, label="Real Function (y = 2x)", color='b')  # Plot the real function
predicted_line, = ax.plot(X, np.zeros_like(X), 'r--', label="Predicted")  # Placeholder for predictions
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Neural Network Learning Approximation of Real Function")

# Train the neural network with live plot updates
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(X_scaled, weights_input_hidden) + bias_hidden
    hidden_layer_output = hidden_layer_input  # No activation for linear behavior

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = output_layer_input  # Final output

    # Calculate mean squared error loss
    error = y_scaled - predicted_output
    loss = np.mean(np.square(error))

    # Backpropagation
    d_predicted_output = error

    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X_scaled.T.dot(d_predicted_output) * learning_rate
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate

    # Update the plot every 1000 epochs
    if epoch % 1000 == 0:
        # Rescale predicted output to original scale
        predicted_output_rescaled = predicted_output * 100.0
        predicted_line.set_ydata(predicted_output_rescaled)  # Update the predicted line

        # Draw updated plot and pause briefly
        plt.draw()
        plt.pause(0.1)  # Pause to allow for real-time update

# Keep the final plot open
plt.ioff()  # Turn off interactive mode
plt.show()
