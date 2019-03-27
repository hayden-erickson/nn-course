import numpy as np
import random as rand
from numpy.linalg import norm
from sklearn.datasets import load_digits


def cost(a, y, derivative=False):
    if derivative:
        return a - y

    return .5*norm(y - a)**2


def softmax(features, derivative=False):
    p = np.exp(features)/sum(np.exp(features))

    if not derivative:
        return p

    # get the derivative
    dp_da = np.outer(-p, p)

    # update the diagonals
    for i in range(len(p)):
        dp_da[i][i] = p[i]*(1-p[i])

#   add up the gradients for each of the activations to each of the probabilities
    return np.sum(dp_da, axis=1)


def linear(features, derivative=False):
    if derivative:
        return np.ones(shape=features.shape)
    return features


def relu(features, derivative=False):
    if derivative:
        return [0 if f < 0 else 1 for f in features]
    return [max(0, f) for f in features]


def avg_cost(features, labels, a, cost_fn):
    costs = [cost_fn(a(x), y) for (x, y) in zip(features, labels)]
    return np.mean(costs)


def label_to_vector(digit):
    probability_vector = np.zeros(10)
    probability_vector[digit] = 1
    return probability_vector


def vector_to_label(vec):
    return np.argmax(vec)


def show_digit_predictions(features, labels, a):
    def predict_to_digit(vec):
        return vector_to_label(a(vec))

    show_predictions(features, labels, predict_to_digit)


def show_predictions(features, labels, a):
    print('prediction\t\tactual')

    def print_row(actual, prediction):
        print('{}\t\t{}'.format(actual, prediction))

    return [print_row(a(x), y) for (x, y) in zip(features, labels)]


class Layer:
    # now we will allow the creation of a layer with the activation function as a parameter
    # that we we can use softmax or any other function instead of just linear
    def __init__(self, num_inputs, num_neurons, activation_fn=linear):
        self.weights = np.random.uniform(-.1, .1,
                                         size=(num_neurons, num_inputs))
        self.biases = np.random.uniform(-.1, .1, size=(num_neurons))
        self.a = activation_fn
        self.da_dz = None

    def predict(self, features):
        z = self.weights.dot(features) + self.biases
        self.da_dz = self.a(z, derivative=True)
        return self.a(z)


class Network:
    def __init__(self, *layers, cost_fn=cost):
        self.layers = layers
        self.dz_dw = []
        self.da_dz = []

    def get_gradient(self, x, y):
        # find the gradient for a single example
        prediction = self.predict(x)
        dC_da = cost(prediction, y, derivative=True)

        dC_dw = []
        dC_db = []

        for i in range(1, len(self.layers)+1):
            dC_dz = dC_da * self.da_dz[-i]
            dC_dw.insert(0, np.outer(dC_dz, self.dz_dw[-(i+1)]))
            dC_db.insert(0, dC_dz)
            dC_da = self.layers[-i].weights.transpose().dot(dC_dz)

        return dC_dw, dC_db

    def predict(self, x):
        da_dz = []
        dz_dw = [x]
        prediction = x

        for l in self.layers:
            prediction = l.predict(prediction)
            da_dz.append(l.da_dz)
            dz_dw.append(prediction)

        self.da_dz = da_dz
        self.dz_dw = dz_dw

        return prediction


def train(net, features, labels, epochs, learning_rate):
    for epoch in range(epochs):
        for (house, price) in zip(features, labels):
            dC_dws, dC_dbs = net.get_gradient(house, price)
            # THIS IS THE LEARNING
            # here we update all the weights and biases
            for j in range(len(net.layers)):
                net.layers[j].weights -= dC_dws[j] * learning_rate
                net.layers[j].biases -= dC_dbs[j].flatten() * learning_rate


#
# Up until now we have used the linear activation function $y = x$. This is fine if our task is regression. In other words if our network is trying to predict continuous values such as house prices or coordinates. However, if we want our network to perform classification, we don't want it to give us a number we want it to give us a class. Specifically, we want the network to tell us what class the input belongs to and the probability.
#
# For instance if we have a network that can distinguish between dogs, cats, and pigs and we give it an image of a dog, we want the network to say that it is confident the image is a dog by means of a percentage value. For example it might give the dog class output a score of 98% and the other two classes a score of 1%. Interpreting this percentage we might say the network is 98% confident the image is a dog.
#
# To do this type of classification we would need three output neurons from the network and we would have to use an activation function that will only give a value between 0 and 1. For our case we can use the sigmoid function.
#
# Because we have a dataset from scikit learn that includes images of handwritten digits, we will use that for our classification network. The handwritten digits dataset has ten different classes as you can imagine, one for each digit 0-9. Therefore, we need a network with 10 output neurons.
#
# As for the inputs of the network, we are using images, but how do we feed an image into the network? we flatten it into a 1 dimensional array and that array becomes a single row in the dataset. The images have 64 pixels meaning the image when viewed is 8X8 pixels.

def cost(a, y, derivative=False):
    if derivative:
        return a - y

    return .5*norm(y - a)**2

# The sigmoid function will only output a number between 0 and 1
# which we can use to represent a probability. It also has the
# very nice property that it's derivative is just s(z)*(1-s(z))
# where s is the sigmoid function.


def sigmoid(z, derivative=False):
    s = 1/(1 + np.exp(-z))

    if not derivative:
        return s

    return s*(1-s)


def linear(z, derivative=False):
    if not derivative:
        return z

    return np.ones(shape=z.shape)


class Layer:
    # now we will allow the creation of a layer with the activation function as a parameter
    # that we we can use softmax or any other function instead of just linear
    def __init__(self, num_inputs, num_neurons, activation_fn=linear):
        self.weights = np.random.uniform(-.1, .1,
                                         size=(num_neurons, num_inputs))
        self.biases = np.random.uniform(-.1, .1, size=(num_neurons))
        self.activation = activation_fn
        self.dz_dw = []
        self.da_dz = []

    def predict(self, features):
        z = self.weights.dot(features) + self.biases
        # here we save the activation function gradient to use later
        # when we perform gradient descent for the whole network
        self.da_dz = self.activation(z, derivative=True)
        self.dz_dw = self.activation(z)
        return self.dz_dw


class Network:
    def __init__(self, *layers):
        self.layers = layers
        self.grad_calls = 0
        self.dz_dw = []
        self.da_dz = []

    def get_gradient(self, x, y):
        # find the gradient for a single example
        prediction = self.predict(x)
        dC_da = cost(prediction, y, derivative=True)

        dC_dw = []
        dC_db = []

        for i in range(1, len(self.layers)+1):
            # the line below is the only difference from our previous
            # network. Instead of assuming that da/dz = 1 (which it
            # does for our linear activation layers) we must use the
            # gradient for any activation that the layer has. In this
            # example it is sigmoid for the last layer.
            dC_dz = dC_da * self.da_dz[-i]
            dC_dw.insert(0, np.outer(dC_dz, self.dz_dw[-(i+1)]))
            dC_db.insert(0, dC_dz)
            dC_da = self.layers[-i].weights.transpose().dot(dC_dz)

        self.grad_calls += 1
        return dC_dw, dC_db

    def predict(self, x):
        da_dz = []
        dz_dw = [x]
        prediction = x

        for l in self.layers:
            prediction = l.predict(prediction)
            da_dz.append(l.da_dz)
            dz_dw.append(prediction)

        self.da_dz = da_dz
        self.dz_dw = dz_dw

        return prediction

# label_to_vector takes in a digit lable 0-9
# and turns it into a vector of probabilities
# where all values are 0 except for the label
# index which is 1. For example, if the label
# were 3, our output vector would have 1 at
# index 3 and 0 everywhere else. i.e.
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]


def label_to_vector(digit):
    probability_vector = np.zeros(10)
    probability_vector[digit] = 1
    return probability_vector

# vector_to_label takes in a vector of probabilities
# where each element corresponds to the probability
# of a digit. For instance, the first value is the
# probability of the input being 0, the second value
# being 1, third being 2, and so on. It finds the
# index with the max probability and returns it.
# Therefore, if our network predicted index 8
# to have the highest value, we would say it has
# predicted the input digit image to be 8. i.e.
# [.01, .02, .31, .22, .14, .06, .02, .1, .93, .4]


def vector_to_label(vec):
    return np.argmax(vec)


def show_predictions(digit_images, digit_labels):
    print('actual\t\tprediction\tcorrect')
    print('------\t\t----------\t-------')
    for (x, y) in zip(digit_images, digit_labels):
        actual = y
        prediction = vector_to_label(net.predict(x))
        print('{}\t\t{}\t\t{}'.format(actual, prediction,
                                      '✓' if actual == prediction else ''))
