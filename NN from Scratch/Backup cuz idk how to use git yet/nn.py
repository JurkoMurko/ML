from Matrix import Matrix
import math
from random import choice

'''these two are kinda perfect for a lambda function, but I think that I might want to call them more that once.'''
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def dsigmoid(y):
    # return sigmoid(x) * (1 - sigmoid(x))
    return y * (1 - y)


class NeuralNetwork:
    learning_rate = 0.2
    training_cycles = 2000

    def __init__(self, num_of_input_nodes, num_of_hidden_nodes, num_of_output_nodes):
        # maybe useful to help this mess of code and this might help with my more than 1 hidden layer problem:
        # w = [Weight() for i in range(2)] that fancy list thing with for and if and stuff

        self.input_nodes = num_of_input_nodes
        self.hidden_nodes = num_of_hidden_nodes
        self.output_nodes = num_of_output_nodes

        #  --------------------------------------------------------------------
        # setting up weights
        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        # setting up nodes
        '''
        these are named numerically from output to input. IK that this is kind of confusing and
        not the best method, but this is meant to change to some sort of a loop so that I could theoretically have
        any number of layers. I just don't know how to do that rn.
        '''
        self.nodes_l1 = Matrix(self.output_nodes, 1)
        self.nodes_l2 = Matrix(self.hidden_nodes, 1)
        self.nodes_l3 = Matrix(self.input_nodes, 1)

        # setting up biases
        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()

    def feed_forward(self, input_list):
        self.nodes_l3.equals(Matrix.convert(input_list))  # array to matrix

        # ---------------------------------------------------------------------------------
        """
        remember you shouldn't have basically the same code twice in the same file/project. that's bad coding
        THESE TWO LAYER CALCULATIONS SHOULD BE IN SOME SORT OF A LOOP
        maybe I should mess with this later to get this to work in 1 line but for now it will do
        """

        # Calculating values of hidden layer
        self.nodes_l2.equals(Matrix.multiply_static(self.weights_ih, self.nodes_l3))  # weights times inputs
        self.nodes_l2.add(self.bias_h)  # add bias
        self.nodes_l2.map(sigmoid)  # activation function

        # Calculating values of output layer
        self.nodes_l1.equals(Matrix.multiply_static(self.weights_ho, self.nodes_l2))  # weights times hidden layer
        self.nodes_l1.add(self.bias_o)  # add bias
        self.nodes_l1.map(sigmoid)  # activation function
        # ---------------------------------------------------------------------------------

        return self.nodes_l1

        # converting back to a list
        # return self.nodes_l1.convert_2()

    def train(self, inputs, targets):
        # outputs = self.feed_forward(inputs)
        #
        # outputs = Matrix.convert(outputs)
        targets = Matrix.convert(targets)

        self.feed_forward(inputs)

        # Errors
        output_errors = Matrix.subtract_matrices(targets, self.nodes_l1)

        weights_ho_t = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.multiply_static(weights_ho_t, output_errors)

        # ----------------------------------------------------------------------------------

        # calculate gradients
        gradients = Matrix.map_static(self.nodes_l1, dsigmoid)
        gradients.element_multiply_matrices(output_errors)
        gradients.multiply_by_num(NeuralNetwork.learning_rate)

        # Calculate Deltas
        hidden_t = Matrix.transpose(self.nodes_l2)
        weights_ho_deltas = Matrix.multiply_static(gradients, hidden_t)

        # ----------------------------------------------------------------------------------

        # calculate gradients
        hidden_gradients = Matrix.map_static(self.nodes_l2, dsigmoid)
        hidden_gradients.element_multiply_matrices(hidden_errors)
        hidden_gradients.multiply_by_num(NeuralNetwork.learning_rate)

        # Calculate Deltas
        input_t = Matrix.transpose(self.nodes_l3)
        weights_ih_deltas = Matrix.multiply_static(hidden_gradients, input_t)

        # ---------------------------------------------------------------------------------

        # adjust the weights
        # print(weights_ho_deltas.values, weights_ih_deltas.values)
        self.weights_ho.add(weights_ho_deltas)
        self.weights_ih.add(weights_ih_deltas)

        # adjust the biases
        # print(gradients.values, hidden_gradients.values)
        self.bias_o.add(gradients)
        self.bias_h.add(hidden_gradients)

        # Ugghghgh why!!! why doesn't it work!!! here's some code for debugging

        print("\ninput: " + str(inputs) + "  target: " + str(targets.values) + "   answer: " + str(nn.feed_forward(inputs).values))
        print("output error: " + str(output_errors.values))


nn = NeuralNetwork(2, 2, 1)

'''
Maybe I should have inputs be put into nn instead of feed_forward. this kinda makes sense cuz its not like your
gonna call feed_forward on a different set of inputs, and it's not like it would work anyways. Also it could get rid 
of having to convert between a matrix and array all the time. also also i need a check to make sure that the number of 
inputs and targets matches the size of the nn
'''

# training data
training_data = [
    {
        "input": [0, 0],
        "target": [0]
    },
    {
        "input": [1, 1],
        "target": [0]
    },
    {
        "input": [1, 0],
        "target": [1]
    },
    {
        "input": [0, 1],
        "target": [1]
    }
]

# training
for _ in range(NeuralNetwork.training_cycles):
    data = choice(training_data)
    nn.train(data['input'], data['target'])

# did we do a good?
a = nn.feed_forward([0, 0]).values
b = nn.feed_forward([1, 1]).values
c = nn.feed_forward([1, 0]).values
d = nn.feed_forward([0, 1]).values

listt = [a, b, c, d]

for yeet in listt:
    print(yeet)

# my failed attempt for the program to just print is it did its job
# for i in training_data:
#     # it can't just be straing equal cuz the nn will never output 0
#     if nn.feedforward(training_data[i]["inputs"][0], training_data[i]["inputs"][1]) == i['target']:
#         print(f'{i["target"]} bueno')
#     else:
#         print("no no")
