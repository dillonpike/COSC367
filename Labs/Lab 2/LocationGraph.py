from search import *
from math import sqrt

class LocationGraph(ExplicitGraph):
    
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes, estimates=None):
        """Initialises an explicit graph.
        Keyword arguments:
        nodes -- a set of nodes
        locations -- a dictionary of nodes to coordinates
        edges -- a sequence of tuples in the form (tail, head) or 
                     (tail, head, cost)
        starting_nodes -- the list of starting nodes. We use a list
                          to remind you that the order can influence
                          the search behaviour.
        goal_node -- the set of goal nodes. It's better if you use a set
                     here to remind yourself that the order does not matter
                     here. This is used only by the is_goal method. 
        """

        # A few assertions to detect possible errors in
        # instantiation. These assertions are not essential to the
        # class functionality.
        assert all(tail in nodes and head in nodes for tail, head, *_ in edges)\
           , "An edge must link two existing nodes!"
        assert all(node in nodes for node in starting_nodes),\
            "The starting_states must be in nodes."
        assert all(node in nodes for node in goal_nodes),\
            "The goal states must be in nodes."

        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
        self.estimates = estimates
        
    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that go out from the given
        node. The action string is automatically generated.

        """
        arcs = set()
        for edge in self.edges:
            tail, head = edge
            cost = sqrt((self.locations[head][0] - self.locations[tail][0])**2 + \
                        (self.locations[head][1] - self.locations[tail][1])**2)
            if tail == node:
                arcs |= {Arc(tail, head, str(tail) + '->' + str(head), cost)}
            elif head == node:
                arcs |= {Arc(head, tail, str(head) + '->' + str(tail), cost)}
        return sorted(arcs)  
    
    
    
def main(): 

    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('C', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})
    
    
    for arc in graph.outgoing_arcs('A'):
        print(arc)
    
    for arc in graph.outgoing_arcs('B'):
        print(arc)
    
    for arc in graph.outgoing_arcs('C'):
        print(arc)    
    
    print()
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
        starting_nodes=['a'],
        goal_nodes={'c'})
    
    for arc in pythagorean_graph.outgoing_arcs('a'):
        print(arc)
    
    print()
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A'), ('C', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})
    
    
    for arc in graph.outgoing_arcs('A'):
        print(arc)
    
    for arc in graph.outgoing_arcs('B'):
        print(arc)
    
    for arc in graph.outgoing_arcs('C'):
        print(arc)
    
    print()
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
        starting_nodes=['a'],
        goal_nodes={'c'})
    
    for arc in pythagorean_graph.outgoing_arcs('a'):
        print(arc)    

if __name__ == '__main__':
    main()