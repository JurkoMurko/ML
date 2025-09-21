from NeuralNetwork import NeuralNetwork
import Training_data

if __name__ == "__main__":
    '''
    Maybe I should have inputs be put into nn instead of feed_forward. this kinda makes sense cuz its not like your
    gonna call feed_forward on a different set of inputs, and it's not like it would work anyways. Also it could get rid 
    of having to convert between a matrix and array all the time. also also i need a check to make sure that the number of 
    inputs and targets matches the size of the nn
    '''
    nn = NeuralNetwork([2, 3, 1])
    NeuralNetwork.learning_rate = 0.025
    NeuralNetwork.training_cycles = 70000

    nn.train(Training_data.xor_training_data)
    nn.xor_grade()
    #nn.cost(Training_data.xor_training_data)

    # nn.save()
    # nn.load()

