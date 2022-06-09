import numpy as np
import itertools

def data_from_string(data_str):
    """Converts data string to a table of data."""
    with_tabs = [list(row.strip()) for row in data_str.splitlines() 
                if row.strip() != '']
    return [[val for val in row if val not in (' ', '\t')] for row in with_tabs]

def construct_node(name, parents, probs):
    """Constructs a node for a belief network."""
    cpt = {tup : prob for tup, prob in zip(itertools.product((True, False), repeat=len(parents)), probs)}
    return {name : {'Parents': parents, 'CPT': cpt}}

def belief_net(data, pseudo_count):
    """Returns a belief network learnt from the data with the class variable
       in the last column.
       Applies laplacian smoothing with the given pseudocount.
       Only works for variables with a domain of two.
    """
    DOMAIN = 2
    true_rows = [row for row in data if row[-1] == 'T']
    false_rows = [row for row in data if row[-1] == 'F']
    
    true_prob = (len(true_rows) + pseudo_count) / (len(data) + DOMAIN * pseudo_count)
    network = construct_node('Y', [], [true_prob])
    
    probs = []
    for i in range(len(data[0]) - 1):
        # Appends tuples to probs for each non-class variable of the form:
        # (True when class variable is true, true when class variable is false)
        prob_true = (list(np.array(true_rows)[:, i]).count('T') + pseudo_count) \
                    / (len(true_rows) + DOMAIN * pseudo_count)
        prob_false = (list(np.array(false_rows)[:, i]).count('T') + pseudo_count) \
                     / (len(false_rows) + DOMAIN * pseudo_count)
        probs.append((prob_true, prob_false))
    
    for i in range(len(probs)):
        network.update(construct_node(f'X{i+1}', ['Y'], probs[i]))
    return network

def main():
    data_str = \
    """
    T	F	F
    F	F	F
    T	F	T
    T	F	T
    T	F	T
    T	T	T
    """
    data = data_from_string(data_str)
    network = belief_net(data, 1)
    print(f"network = {network}") 
    
    data_str = \
    """
    T	F	F
    F	F	F
    F	T	F
    F	F	T
    F	F	T
    F	F	T
    F	T	T
    """
    data = data_from_string(data_str)
    network = belief_net(data, 2)
    print(f"network = {network}") 
    
    data_str = \
    """
    T	T	F	F
    T	F	F	F
    T	T	F	F
    T	F	F	T
    F	F	F	T
    F	T	F	T
    F	F	F	T
    """
    data = data_from_string(data_str)
    network = belief_net(data, 2)
    print(f"network = {network}") 
    
    data_str = \
    """
    T	F	F	F
    F	F	F	F
    T	F	F	F
    F	F	F	F
    F	F	F	T
    F	F	F	T
    T	T	F	T
    """
    data = data_from_string(data_str)
    network = belief_net(data, 1)
    print(f"network = {network}")     
    
if __name__ == '__main__':
    main()