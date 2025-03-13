import numpy as np

# Input data (features) and output (targets) for a linear relationship
X = np.array([[1], [2], [3], [4], [5], [6], [7]], dtype=np.float32)
y = np.array([[2], [4], [6], [8], [10], [12], [14]], dtype=np.float32)

# Scale data to improve network training stability
X = X / 100.0
y = y / 100.0

# Neural network hyperparameters
input_size = 1
hidden_size = 1  # Single hidden neuron since we're modeling a linear relationship
output_size = 1
learning_rate = 0.01
epochs = 500000

# Initialize weights and biases
np.random.seed(1)
weights_input_hidden = np.random.rand(input_size, hidden_size)
weights_hidden_output = np.random.rand(hidden_size, output_size)
bias_hidden = np.random.rand(1, hidden_size)
bias_output = np.random.rand(1, output_size)

# Training the neural network
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = hidden_layer_input  # No activation for linear behavior

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = output_layer_input  # Direct linear output

    # Calculate mean squared error loss
    error = y - predicted_output
    loss = np.mean(np.square(error))

    # Backpropagation
    d_predicted_output = error  # Directly using the error for the gradient

    # Calculate gradients for weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X.T.dot(d_predicted_output) * learning_rate
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate

    # Print the loss every 1000 epochs
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

# Test the network with a new input
x_new = np.array([[99]], dtype=np.float32) / 100.0
hidden_layer_input_new = np.dot(x_new, weights_input_hidden) + bias_hidden
hidden_layer_output_new = hidden_layer_input_new

output_layer_input_new = np.dot(hidden_layer_output_new, weights_hidden_output) + bias_output
predicted_output_new = output_layer_input_new * 100.0  # Scale back to original range

print(f"The predicted value for x = 99 is: {predicted_output_new[0][0]}")
