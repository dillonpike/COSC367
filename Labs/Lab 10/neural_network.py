def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given parameters."""
    def perceptron(input):
        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        output = sum(weights[i] * input[i] for i in range(len(weights))) + bias
        
        return int(output >= 0)
    
    return perceptron # this line is fine

def accuracy(classifier, inputs, expected_outputs):
    outputs = [classifier(inp) for inp in inputs]
    return sum([1 for i in range(len(outputs)) 
                if outputs[i] == expected_outputs[i]]) / len(outputs)

def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    for i in range(max_epochs):
        for inp, target in training_examples:
            perceptron = construct_perceptron(weights, bias)
            output = perceptron(inp)
            for j in range(len(weights)):
                weights[j] += learning_rate * inp[j] * (target - output)
            bias += learning_rate * (target - output)
            print(weights, bias)
    return (weights, bias)

def main():
    perceptron = construct_perceptron([-1, 3], 2)
    inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
    targets = [0, 1, 1, 0]
    
    print(accuracy(perceptron, inputs, targets))
    
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
      ((0, 0), 0),
      ((0, 1), 0),
      ((1, 0), 0),
      ((1, 1), 1),
      ]
    max_epochs = 50
    
    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")
    
    perceptron = construct_perceptron(weights, bias)
    
    print(perceptron((0,0)))
    print(perceptron((0,1)))
    print(perceptron((1,0)))
    print(perceptron((1,1)))
    print(perceptron((2,2)))
    print(perceptron((-3,-3)))
    print(perceptron((3,-1)))
    
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
      ((0, 0), 0),
      ((0, 1), 1),
      ((1, 0), 1),
      ((1, 1), 0),
      ]
    max_epochs = 50
    
    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")
    
    weights = [-1, 1]
    bias = 0
    learning_rate = 0.5
    examples = [
        ([-2, 0], 0),    # index 0 (first example)
        ([-1, 1], 0),
        ([1, 1], 0),
        ([2, 0], 1),
        ([1, -1], 1),
        ([-1, -1], 1),
    ]
    
    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")    
    
if __name__ == '__main__':
    main()