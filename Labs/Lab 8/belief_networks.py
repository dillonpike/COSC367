from itertools import product

def joint_prob(network, assignment):
    p = 1 # p will enentually hold the value we are interested in
    for var in network:
        # Extract the probability of var=true from the network
        # by finding the right assignment for Parents and getting the
        # corresponding CPT. 
        
        # Update p by multiplying it by probablity var=true or var=false
        # depending on how var appears in the given assignment.
        tup = tuple(assignment[parent] for parent in network[var]['Parents'])
        if assignment[var] is True:
            p *= network[var]['CPT'][tup]
        else:
            p *= (1 - network[var]['CPT'][tup])
        
    return p

def query(network, query_var, evidence):
    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    
    # Initialise a raw distribution to [0, 0]
    raw_distribution = [0, 0]
    
    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        # Update the assignment to include the query variable
        assignment[query_var] = query_value
        for values in product((True, False), repeat=len(hidden_vars)):
            # Update the assignment (we now have a complete assignment)
            for var,val in zip(hidden_vars, values):
                assignment[var] = val
            # Update the raw distribution by the probability of the assignment.
            raw_distribution[query_value] += joint_prob(network, assignment)
            
    # Normalise the raw distribution and return it
    total = sum(raw_distribution)
    return list(map(lambda x: x / total, raw_distribution))



def main():
    network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
    }
    
    answer = query(network, 'A', {})
    print("P(A=true) = {:.5f}".format(answer[True]))
    print("P(A=false) = {:.5f}".format(answer[False]))
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
                }},
                
        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
                }},
        }
     
    answer = query(network, 'B', {'A': False})
    print("P(B=true|A=false) = {:.5f}".format(answer[True]))
    print("P(B=false|A=false) = {:.5f}".format(answer[False]))
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
                }},
                
        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
                }},
        }
     
    answer = query(network, 'B', {})
    print("P(B=true) = {:.5f}".format(answer[True]))
    print("P(B=false) = {:.5f}".format(answer[False]))
    
    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
                }},
                
        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
                }},
        'Alarm': {
            'Parents': ['Burglary','Earthquake'],
            'CPT': {
                (True,True): 0.95,
                (True,False): 0.94,
                (False,True): 0.29,
                (False,False): 0.001,
                }},
    
        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
                }},
    
        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
                }},
        }
    
    answer = query(network, 'Burglary', {'John': True, 'Mary': True})
    print("Probability of a burglary when both\n"
          "John and Mary have called: {:.3f}".format(answer[True]))
    
    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
                }},
                
        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
                }},
        'Alarm': {
            'Parents': ['Burglary','Earthquake'],
            'CPT': {
                (True,True): 0.95,
                (True,False): 0.94,
                (False,True): 0.29,
                (False,False): 0.001,
                }},
    
        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
                }},
    
        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
                }},
        }
    
    answer = query(network, 'John', {'Mary': True})
    print("Probability of John calling if\n"
          "Mary has called: {:.5f}".format(answer[True]))
    
    network = {
        'Disease': {
            'Parents': [],
            'CPT': {
                (): 1/100000
                }},
                
        'Test': {
            'Parents': ['Disease'],
            'CPT': {
                (True,): 0.99,
                (False,): 0.01,
                }},
        }
    
    answer = query(network, 'Disease', {'Test': True})
    print("The probability of having the disease\n"
          "if the test comes back positive: {:.8f}"
          .format(answer[True]))
    
    answer = query(network, 'Disease', {'Test': False})
    print("The probability of having the disease\n"
          "if the test comes back negative: {:.8f}"
          .format(answer[True]))
    
    network = {
        'Virus': {
            'Parents': [],
            'CPT': {
                (): 0.01
                }},
                
        'A': {
            'Parents': ['Virus'],
            'CPT': {
                (True,): 0.95,
                (False,): 0.1,
                }},
                
        'B': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},
        }
    
    answer = query(network, 'Virus', {'A': True})
    print("The probability of carrying the virus\n"
          "if test A is positive: {:.5f}"
          .format(answer[True]))
    
    answer = query(network, 'Virus', {'B': True})
    print("The probability of carrying the virus\n"
          "if test B is positive: {:.5f}"
          .format(answer[True]))
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2 # You can change this value
                }
        },
            
        'B': {
            'Parents': [],
            'CPT': {
                (): 0.2 # You can change this value
                }
        },
        
        'C': {
            'Parents': [],
            'CPT': {
                (): 0.2 # You can change this value
                }
        },
            
        'D': {
            'Parents': ['B'],
            'CPT': {
                (False,): 0.2, # You can change this value
                (True,): 0.3
                }
        },
            
        'E': {
            'Parents': ['B'],
            'CPT': {
                (False,): 0.4, # You can change this value
                (True,): 0.5
                }
        }
    }
    
    answer = query(network, 'D', {'B': True, 'E': True})
    print("P(D=true|B=True,E=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'D', {'B': True, 'E': False})
    print("P(D=true|B=True,E=False) = {:.5f}".format(answer[True]))
    answer = query(network, 'E', {'B': True, 'D': True})
    print("P(E=true|B=True,D=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'E', {'B': True, 'D': False})
    print("P(E=true|B=True,D=False) = {:.5f}".format(answer[True]))
    answer = query(network, 'D', {'B': False, 'E': True})
    print("P(D=true|B=False,E=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'D', {'B': False, 'E': False})
    print("P(D=true|B=False,E=False) = {:.5f}".format(answer[True]))    
    answer = query(network, 'E', {'B': False, 'D': True})
    print("P(E=true|B=False,D=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'E', {'B': False, 'D': False})
    print("P(E=true|B=False,D=False) = {:.5f}".format(answer[True]))
    
    answer = query(network, 'D', {'B': True})
    print("P(D=true|B=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'D', {'B': False})
    print("P(D=true|B=False) = {:.5f}".format(answer[True]))
    answer = query(network, 'E', {'B': True})
    print("P(E=true|B=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'E', {'B': False})
    print("P(E=true|B=False) = {:.5f}".format(answer[True]))      
    
    print(sorted(network.keys()))
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
                }},
        'B': {
            'Parents': ['A'],
            'CPT': {
                (False,): 0.2,
                (True,): 0.3
                }},
                
        'C': {
            'Parents': ['A'],
            'CPT': {
                (False,): 0.4,
                (True,): 0.4
                }},
    }

    answer = query(network, 'B', {'A': True, 'C': True})
    print("P(B=true|A=True,C=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'B', {'A': True, 'C': False})
    print("P(B=true|A=True,C=False) = {:.5f}".format(answer[True]))
    answer = query(network, 'B', {'A': False, 'C': True})
    print("P(B=true|A=False,C=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'B', {'A': False, 'C': False})
    print("P(B=true|A=False,C=False) = {:.5f}".format(answer[True]))
    answer = query(network, 'B', {'A': True})
    print("P(B=true|A=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'B', {'A': False})
    print("P(B=true|A=False) = {:.5f}".format(answer[True]))
    print()
    answer = query(network, 'C', {'A': True, 'B': True})
    print("P(C=true|A=True,B=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'C', {'A': True, 'B': False})
    print("P(C=true|A=True,B=False) = {:.5f}".format(answer[True]))
    answer = query(network, 'C', {'A': False, 'B': True})
    print("P(C=true|A=False,B=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'C', {'A': False, 'B': False})
    print("P(C=true|A=False,B=False) = {:.5f}".format(answer[True]))
    answer = query(network, 'C', {'A': True})
    print("P(C=true|A=True) = {:.5f}".format(answer[True]))
    answer = query(network, 'C', {'A': False})
    print("P(C=true|A=False) = {:.5f}".format(answer[True]))     
    

if __name__ == '__main__':
    main()