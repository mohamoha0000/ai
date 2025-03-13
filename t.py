import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize input data (number pairs) and labels (1 for odd, 0 for even)
X = np.array([[i] for i in range(1, 101)])  # Training data from 1 to 100
y = np.array([[1 if i % 2 != 0 else 0] for i in range(1, 101)])  # 1 for odd, 0 for even

# Initialize weights and biases
np.random.seed(1)
input_size = X.shape[1]
hidden_size = 3  # Hidden layer with 3 neurons
output_size = 1  # Output layer with 1 neuron

# Randomly initialize weights
weights_input_hidden = np.random.rand(input_size, hidden_size)
weights_hidden_output = np.random.rand(hidden_size, output_size)

# Bias initialization
bias_hidden = np.random.rand(1, hidden_size)
bias_output = np.random.rand(1, output_size)

# Learning rate
lr = 0.1

# Training the neural network
epochs = 100000
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)

    # Calculate the error
    error = y - predicted_output

    # Backpropagation
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * lr
    weights_input_hidden += X.T.dot(d_hidden_layer) * lr
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

    # Print the loss every 1000 epochs
    if epoch % 10000 == 0:
        loss = np.mean(np.abs(error))
        print(f"Epoch {epoch}, Loss: {loss}")

# Testing the network with new numbers
while True:
    x_new = np.array([[int(input("Enter a number: "))]])  # Input a new number to test
    hidden_layer_input_new = np.dot(x_new, weights_input_hidden) + bias_hidden
    hidden_layer_output_new = sigmoid(hidden_layer_input_new)
    output_layer_input_new = np.dot(hidden_layer_output_new, weights_hidden_output) + bias_output
    predicted_output_new = sigmoid(output_layer_input_new)
    prediction = round(predicted_output_new[0][0])
    print(f"The predicted value for x = {x_new[0][0]} is: {'Odd' if prediction == 1 else 'Even'}")