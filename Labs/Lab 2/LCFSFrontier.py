from search import *
from heapq import *
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

class LCFSFrontier(Frontier):
    
    def __init__(self):
        self.container = []
    
    def add(self, path):
        cost = sum(arc.cost for arc in path)
        heappush(self.container, (cost, path))
        print(f"+ {path_string(path)}, {cost}")
        
    def __next__(self):
        if len(self.container) > 0:
            popped = heappop(self.container)
            print(f"- {path_string(popped[1])}, {popped[0]}")
            return popped[1]
        else:
            raise StopIteration
        
def path_string(path):
    path_string = ''
    for arc in path:
        path_string += arc.head
    return path_string        

def main(): 
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A'), ('C', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
        starting_nodes=['a'],
        goal_nodes={'c'})
    
    solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
    print_actions(solution)
    
    print()
    graph = ExplicitGraph(
        nodes={'A', 'B', 'C', 'D', 'G'},
        edge_list=[('A', 'B', 2), ('A', 'C', 3), ('B', 'D', 5),
                   ('C', 'D', 5), ('D', 'G', 3),],
        starting_nodes=['A'],
        goal_nodes = {'G'},
        )
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    g = 'g'
    graph = ExplicitGraph(
        nodes={a, b, c, d, g},
        edge_list=[(a,b,4), (a,c,2), (a,d,1),
         (b,g,4), (c,g,2), (d,g,4)],
        starting_nodes = [a],
        goal_nodes = {g}
        ) 
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    graph = ExplicitGraph(
        nodes={'S', 'C', 'G'},
        edge_list=[('C','G',3), ('C','S',2), ('G','C',3),
         ('G','S',7), ('S','C',2), ('S','G',7)],
        starting_nodes = ['S'],
        goal_nodes = {'G'}
        ) 
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    graph = ExplicitGraph(
        nodes={'A', 'B', 'C', 'D', 'G'},
        estimates={'A':5, 'B':5, 'C':9, 'D':1, 'G':0},
        edge_list=[('A','B',2), ('A','C',3), ('B','D',5), ('C','D',10), ('D','G',3)],
        starting_nodes=['A'],
        goal_nodes={'G'},
        )
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

if __name__ == '__main__':
    main()