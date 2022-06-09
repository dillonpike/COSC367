from random import randrange
import time

def is_valid_expression(object, function_symbols, leaf_symbols):
    if type(object) == int or object in leaf_symbols:
        return True
    elif type(object) == list and len(object) == 3:
        return object[0] in function_symbols and \
               is_valid_expression(object[1], function_symbols, leaf_symbols) and \
               is_valid_expression(object[2], function_symbols, leaf_symbols)
    else:
        return False
    
def depth(expression):
    if type(expression) in (int, str):
        return 0
    else:
        return 1 + max(depth(expression[1]), depth(expression[2]))
    
def evaluate(expression, bindings):
    if type(expression) == int:
        return expression
    elif type(expression) == str:
        return bindings[expression]
    else:
        return bindings[expression[0]](evaluate(expression[1], bindings), 
                                       evaluate(expression[2], bindings))
    
def random_expression(function_symbols, leaves, max_depth, depth=0):
    if randrange(2) == 0 or depth == max_depth:
        return leaves[randrange(len(leaves))]
    else:
        return [function_symbols[randrange(len(function_symbols))],
                random_expression(function_symbols, leaves, max_depth, depth+1),
                random_expression(function_symbols, leaves, max_depth, depth+1)]
    
def generate_rest(initial_sequence, expression, length):
    sequence = []
    bindings_sequence = initial_sequence + sequence
    n = len(initial_sequence)
    bindings = {'+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y}
    for i in range(n, n + length):
        bindings.update({'x': bindings_sequence[i-2], 'y': bindings_sequence[i-1], 'i': i})
        next_element = evaluate(expression, bindings)
        sequence.append(next_element)
        bindings_sequence.append(next_element)
    return sequence

def predict_rest(sequence):
    n = len(sequence) // 2 - 1
    leaves = ['x', 'y', 'i'] + [i for i in range(-2, 3)]
    function_symbols = ['+', '-', '*']
    initial_sequence = sequence[:n]
    testing_sequence = sequence[n:]
    while True:
        expression = random_expression(function_symbols, leaves, 3)
        test_rest = generate_rest(initial_sequence, expression, len(sequence)-n)
        if testing_sequence == test_rest:
            rest = generate_rest(sequence, expression, 5)
            return rest

def is_valid_expression_tests():
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 1
    
    print(is_valid_expression(expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'y'
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 2.0
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 123, 'x']
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', ['+', 0, -1], ['f', 1, 'x']]
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['+', ['f', 1, 'x'], -1]
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y', -1, 0, 1]
    expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'f'
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 1, 0, -1]
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['x', 0, 1]
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbolsfunction_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['g', 0, 'y']
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
def depth_tests():
    expression = 12
    print(depth(expression))
    
    expression = 'weight'
    print(depth(expression))

    expression = ['add', 12, 'x']
    print(depth(expression))

    expression = ['add', ['add', 22, 'y'], 'x']
    print(depth(expression))
    
    expression = ['+',
                   ['*', 2, 'i'],
                   ['*',
                     ['*', -3, ['*', -3, 'x']],
                     'x']]
    
    print(depth(expression))
    
def evaluate_tests():
    bindings = {}
    expression = 12
    print(evaluate(expression, bindings))
    
    bindings = {'x':5, 'y':10, 'time':15}
    expression = 'y'
    print(evaluate(expression, bindings))
    
    bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
    expression = ['add', 12, 'x']
    print(evaluate(expression, bindings))
    
    import operator
    
    bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
    expression = ['add', ['add', 22, 'y'], 'x']
    print(evaluate(expression, bindings))
    
def check_distinctness(expressions):
    distinct_expressions = []
    for expression in expressions:
        if expression not in distinct_expressions:
            distinct_expressions.append(expression)
    if len(distinct_expressions) >= 1000:
        print("OK")
    else:
        print("Fewer than 1000 distinct expressions.")
    
def check_diversity(expressions, max_depth):
    depth_counter = [0 for i in range(max_depth+1)]
    for expression in expressions:
        depth_counter[depth(expression)] += 1
    depth_bool = [count >= 100 for count in depth_counter]
    if all(depth_bool):
        print("OK")
    else:
        print("Fewer than 100 expressions at each depth.")
    
def random_expression_tests():
    function_symbols = ['f', 'g', 'h']
    constant_leaves =  list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 4
    
    for _ in range(10000):
        expression = random_expression(function_symbols, leaves, max_depth)
        if not is_valid_expression(expression, function_symbols, leaves):
            print("The following expression is not valid:\n", expression)
            break
    else:
        print("OK")
        
    expressions = [random_expression(function_symbols, leaves, max_depth)
                   for _ in range(10000)]
    
    # Out of 10000 expressions, at least 1000 must be distinct
    check_distinctness(expressions)
    
    expressions = [random_expression(function_symbols, leaves, max_depth)
                   for _ in range(10000)]
    
    # Out of 10000 expressions, there must be at least 100 expressions
    # of depth 0, 100 of depth 1, ..., and 100 of depth 4.
    
    check_diversity(expressions, max_depth)
    
def generate_rest_tests():
    initial_sequence = [0, 1, 2]
    expression = 'i' 
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression,
                        length_to_generate))
    
    # no particular pattern, just an example expression
    initial_sequence = [-1, 1, 367]
    expression = 'i' 
    length_to_generate = 4
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))
    
    initial_sequence = [4, 6, 8, 10]
    expression = ['*', ['+', 'i', 2], 2]
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    initial_sequence = [4, 6, 8, 10]
    expression = ['+', 2, 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    initial_sequence = [0, 1]
    expression = 'x'
    length_to_generate = 6
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    # Fibonacci sequence
    initial_sequence = [0, 1]
    expression = ['+', 'x', 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    initial_sequence = [367, 367, 367]
    expression = 'y'
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    # no pattern, just a demo
    initial_sequence = [0, 1, 2]
    expression = -1 
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
    initial_sequence = [0, 1, 2]
    expression = 'i'
    length_to_generate = 0
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
def predict_rest_tests():
    #from random import seed
    #seed(1)
    sequence = [0, 1, 2, 3, 4, 5, 6, 7]
    the_rest = predict_rest(sequence)
    print(sequence)
    print(the_rest)
    
    sequence = [0, 2, 4, 6, 8, 10, 12, 14]
    print(predict_rest(sequence))
    
    sequence = [31, 29, 27, 25, 23, 21]
    print(predict_rest(sequence))
    
    sequence = [0, 1, 4, 9, 16, 25, 36, 49]
    print(predict_rest(sequence))
    
    sequence = [3, 2, 3, 6, 11, 18, 27, 38]
    print(predict_rest(sequence))
    
    sequence =  [0, 1, 1, 2, 3, 5, 8, 13]
    print(predict_rest(sequence))
    
    sequence = [0, -1, 1, 0, 1, -1, 2, -1]
    print(predict_rest(sequence))
    
    sequence = [1, 3, -5, 13, -31, 75, -181, 437]
    print(predict_rest(sequence))
    
def test_timing():
    max_time = 0
    avg_time = 0
    count = 0
    iterations = 100
    for i in range(iterations):
        start_time = time.time()
        is_valid_expression_tests()
        depth_tests()
        evaluate_tests()
        random_expression_tests()
        generate_rest_tests()        
        predict_rest_tests()
        end_time = time.time()
        time_taken = end_time-start_time
        max_time = max(max_time, time_taken)
        avg_time += time_taken / iterations
        if (end_time-start_time) >= 2:
            count += 1
    print(f"Maximum time taken: {max_time:.4f}")
    print(f"Average time taken: {avg_time:.4f}")
    print(f"Percentage of time over 2 second time limit: {count/iterations:.4f}%")
    
def tricky_test():
    for i in range(100):
        sequence = [0, -1, 1, 0, 1, -1, 2, -1]
        if predict_rest(sequence) != [5, -4, 29, -13, 854]:
            print("Wrong.")    
    
if __name__ == '__main__':
    is_valid_expression_tests()
    depth_tests()
    evaluate_tests()
    random_expression_tests()
    generate_rest_tests()
    print()
    predict_rest_tests()
    #test_timing()
    tricky_test()