import numpy as np
import matplotlib.pyplot as plt

# Input data (features) and output (targets) for a non-linear relationship
X = np.array([[10], [20], [30], [40], [50], [60], [70],[80]], dtype=np.float32)
y = np.array([[10], [20], [30], [40], [30], [20], [10],[0]], dtype=np.float32)

# Scale data to improve network training stability
X_scaled = X / 10.0  # Scale to a smaller range to improve learning
y_scaled = y / 10.0

# Neural network hyperparameters
input_size = 1
hidden_size = 100  # Increase hidden size to capture non-linear patterns
output_size = 1
learning_rate = 0.001  # Smaller learning rate for stability
epochs = 500000

# Initialize weights and biases with random values
np.random.seed(1)
weights_input_hidden = np.random.randn(input_size, hidden_size) * 0.1
weights_hidden_output = np.random.randn(hidden_size, output_size) * 0.1
bias_hidden = np.zeros((1, hidden_size))
bias_output = np.zeros((1, output_size))

# Activation function (ReLU) and its derivative for the hidden layers
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

# Set up the plot for real-time visualization
plt.ion()  # Interactive mode on
fig, ax = plt.subplots()
ax.plot(X, y, label="Real Function", color='b')  # Target function
predicted_line, = ax.plot(X, np.zeros_like(X), 'r--', label="Predicted")  # Placeholder for predictions
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Neural Network Learning Approximation of Non-linear Function")

# Train the neural network with live plot updates
for epoch in range(epochs):
    # Forward propagation through hidden layer
    hidden_layer_input = np.dot(X_scaled, weights_input_hidden) + bias_hidden
    hidden_layer_output = relu(hidden_layer_input)  # Apply ReLU activation

    # Forward propagation to output layer
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = output_layer_input  # Linear output layer for regression

    # Calculate mean squared error loss
    error = y_scaled - predicted_output
    loss = np.mean(np.square(error))

    # Print loss every 1000 epochs
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

    # Backpropagation
    d_predicted_output = error  # Derivative of loss w.r.t. predicted output

    # Gradient for weights and biases from hidden layer to output
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate

    # Backpropagate through hidden layer
    d_hidden_layer = d_predicted_output.dot(weights_hidden_output.T) * relu_derivative(hidden_layer_input)
    weights_input_hidden += X_scaled.T.dot(d_hidden_layer) * learning_rate
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

    # Update the plot every 1000 epochs
    if epoch % 1000 == 0:
        # Rescale predicted output to original scale
        predicted_output_rescaled = predicted_output * 10.0  # Scale back to match the original `y`
        predicted_line.set_ydata(predicted_output_rescaled)  # Update the predicted line in plot

        # Draw updated plot and pause briefly for real-time visualization
        plt.draw()
        plt.pause(0.1)  # Pause to update the plot

# Keep the final plot open after training
plt.ioff()  # Turn off interactive mode
plt.show()
