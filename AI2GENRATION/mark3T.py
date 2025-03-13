import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Normalize input data (X) and target output (y)
X = np.array([[1], [2], [3], [4], [5], [6], [7]]) / 100.0
y = np.array([[2], [4], [6], [8], [10], [12], [14]]) / 100.0

# Initialize weights and biases
np.random.seed(1)
input_size = X.shape[1]
hidden_size = 1
output_size = 1

weights_input_hidden = np.random.rand(input_size, hidden_size)
weights_hidden_output = np.random.rand(hidden_size, output_size)
bias_hidden = np.random.rand(1, hidden_size)
bias_output = np.random.rand(1, output_size)

# Learning rate and reduced epochs
lr = 0.01
epochs = 500000

# Training the neural network
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)  # Activation only in hidden layer

    # Linear output layer
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = output_layer_input  # No activation here

    # Calculate the error
    error = y - predicted_output
    loss = np.mean(np.square(error))

    # Backpropagation
    d_predicted_output = error  # Direct error as gradient for linear output

    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * lr
    weights_input_hidden += X.T.dot(d_hidden_layer) * lr
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

    # Print the loss every 1000 epochs
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

# Testing the network with a new input
x_new = np.array([[99]]) / 100.0
hidden_layer_input_new = np.dot(x_new, weights_input_hidden) + bias_hidden
hidden_layer_output_new = sigmoid(hidden_layer_input_new)

output_layer_input_new = np.dot(hidden_layer_output_new, weights_hidden_output) + bias_output
predicted_output_new = output_layer_input_new * 100.0  # Scale back to original range

print(f"The predicted value for x = 99 is: {predicted_output_new[0][0]}")
