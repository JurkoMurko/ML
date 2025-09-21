from Matrix import Matrix
import math
from random import choice, randint
import ast


class NeuralNetwork:
    learning_rate = 0.1
    training_cycles = 5000

    def __init__(self, shape_list):
        self.shape = shape_list
        self.num_of_layers = len(self.shape)
        self.num_of_weights = len(self.shape) - 1
        self.num_of_biases = self.num_of_weights

        self.nodes = [Matrix(self.shape[i], 1) for i in range(self.num_of_layers)]

        # I need to turn this into something readable

        '''
        ok rn im realizing that oop is stupid. 
        Like do you really want me to hava a class for each of the types of things in a NN?!!!!!!!!!!!!!!!!!!
        that just doesn't seam right. stuff like this should have elegence,
        kinda like math, but the idea of all these objects just doesn't feel right
        '''

        # create lists of matrices for the weights and biases
        self.weights = [Matrix(self.shape[i + 1], self.shape[i]) for i in range(self.num_of_weights)]
        self.bias = [Matrix(self.shape[i + 1], 1) for i in range(self.num_of_weights)]

        # randomeize the weights and biases
        for weight_matrix, bias_matrix in self.weights, self.bias:
            weight_matrix.randomize()
            bias_matrix.randomize()
        
        self.nodes[0].randomize() 

    def feed_forward(self, list_of_input_values):
        self.nodes[0].equals(Matrix.convert(list_of_input_values))  # array to matrix

        '''
        This can be written better I just don't know how.
        Maybe take a hint from functional programming and turn it into a clean function looking thing. Idk.
        '''
        # feed forward loop
        for i in range(1, self.num_of_layers):
            self.nodes[i].equals(Matrix.multiply_static(self.weights[i - 1], self.nodes[i - 1]))  # weights times inputs
            self.nodes[i].add(self.bias[i - 1])  # add bias
            self.nodes[i].map(lambda x : 1 / (1 + math.exp(-x)))  # activation function
        
        return self.nodes[-1].convert_2()  # returning the list version of the output

    def calculate_errors(self, targets):
            errors = []
            errors.append(Matrix.subtract_matrices(targets, self.nodes[-1]))

            # ik all this number stuff and subtraction is confusing. basically its all done relative to the layers
            for i in range(self.num_of_layers - 1, 1, -1):
                errors.append(Matrix.multiply_static(Matrix.transpose(self.weights[i - 1]), errors[-1]))

            errors.reverse()
            return errors

    def backprop(self, input_values, targets):
        self.feed_forward(input_values)
        targets = Matrix.convert(targets) # convert list into Matrix

        # backprop loop
        for i in range(self.num_of_weights, 0, -1):
            errors = self.calculate_errors(targets)  # getting the errors

            # calculate gradients
            gradient = Matrix.map_static(self.nodes[i], lambda y : y * (1 - y))
            gradient.element_multiply_matrices(errors[i - 1])
            gradient.multiply_by_num(NeuralNetwork.learning_rate)

            # Calculate Deltas
            hidden_t = Matrix.transpose(self.nodes[i - 1])
            weight_deltas = Matrix.multiply_static(gradient, hidden_t)

            # adjusting the weights and biases
            self.weights[i - 1].add(weight_deltas)
            self.bias[i - 1].add(gradient)

    def train(self, training_data):
        for i in range(NeuralNetwork.training_cycles):
            data = choice(training_data)
            self.backprop(data['input'], data['target'])

    def xor_grade(self):
        # mmmmmm this only works with one output
        # also i need a progress bar that doesn't slow the program down to nothing
        # also also this doesn't work with any other problem than xor

        # cost_list = []

        for i in range(2):
            for j in range(2):
                if i + j == 0 or i + j == 2:
                    target = 0
                else: 
                    target = 1
                
                guess = self.feed_forward([i, j])[0]
                error = target - guess
                grade = round((1 - (abs(error))) * 100, 2)
                # cost_list.append(error ** 2)
                
                print(f"input: {[i, j]} grade: {grade}% of the way there")

    # def cost(training_data):
    #     break
    #     for item in training_data:

    #     error = targets - NeuralNetwork.feed_forward(inputs)
    #     print(NeuralNetwork.calculate_errors())

        
        
        # cost = sum(cost_list) / len(cost_list)
        # print(f"Cost: {cost}")

        # print(self.feed_forward([0, 0]))
        # print(self.feed_forward([0, 1]))
        # print(self.feed_forward([1, 0]))
        # print(self.feed_forward([1, 1]))    

    # we need a way to save the state of the weights and then load it
    def save(self):
        # save the values of the weights
        with open(r"C:\Users\jurko\Desktop\Programming\ML\save\weights.txt", "w") as f:
            for i in range(self.num_of_weights):
                f.write(str(self.weights[i].values) + "\n")

        # save the values of the Biases
        with open(r"C:\Users\jurko\Desktop\Programming\ML\save\biases.txt", "w") as f:
            for i in range(self.num_of_weights):
                f.write(str(self.bias[i].values) + "\n")
                
        # save the shape of the Neural Network
        with open(r"C:\Users\jurko\Desktop\Programming\ML\save\shape.txt", "w") as f:
            f.write(str(self.shape))

    # def load(self):
    #     with open("save.py", "r") as f:
    #         c = f.read()

    #         # init
    #         print(type(c.split("\n")[0].split(": ")[1]))
    #         self.arch = ast.literal_eval(c.split("\n")[0].split(": ")[1])
    #         self.num_of_layers = len(self.arch)
    #         self.num_of_weights = len(self.arch) - 1

    #         self.weights.clear
    #         self.nodes.clear
    #         self.bias.clear

    #         self.weights = [Matrix(self.arch[i + 1], self.arch[i]) for i in range(self.num_of_weights)]
    #         self.nodes = [Matrix(self.arch[i], 1) for i in range(self.num_of_layers)]
    #         self.bias = [Matrix(self.arch[i + 1], 1) for i in range(self.num_of_weights)]

    #         # setting up weights and biases
    #         for i in range(self.num_of_weights):
    #             self.weights[i].values = c.split("\n")[1 + (i * 2)].split(": ")[1]
    #             self.bias[i].values = c.split("\n")[2 + (i * 2)].split(": ")[1]

    #         # the ideal load function
    #         for set in range(self.num_of_weights):
    #             for row in range(self.arch[set + 1]):
    #                 for col in range(self.arch[set]):
    #                     self.weights[set][row][col] =  

    #         # setting up nodes
    #         for i in range(self.num_of_layers):
    #             self.nodes.append(Matrix(self.arch[i], 1))
