from search import *
from heapq import *
from math import sqrt

def generic_search(graph, frontier):
    """Implements a generic graph search algorithm (see the lecture
    notes). The actual search behaviour depends on the type of the
    frontier object.

    """

    for starting_node in graph.starting_nodes():
        # Paths are tuples and the first arc on each path is a dummy
        # arc to a starting node
        frontier.add((Arc(None, starting_node, "no action", graph.estimates[starting_node]),), graph.estimates[starting_node]) 
    
    for path in frontier:
        node_to_expand = path[-1].head # head of the last arc in the path

        if graph.is_goal(node_to_expand):
            yield path

        for arc in graph.outgoing_arcs(node_to_expand):
            frontier.add(path + (arc,), graph.estimates[arc.head]) # add back a new extended path

class AStarGraph(ExplicitGraph):
        
    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that go out from the given
        node. The action string is automatically generated.

        """
        arcs = []
        for edge in self.edge_list:
            if len(edge) == 2:  # if no cost is specified
                tail, head = edge
                cost = 1        # assume unit cost
            else:
                tail, head, cost = edge
            cost -= self.estimates[tail]
            cost += self.estimates[head]
            if tail == node:
                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), cost))
        return arcs

class AStarFrontier(Frontier):
    
    def __init__(self):
        self.container = []
    
    def add(self, path, head_estimate):
        cost = sum(arc.cost for arc in path)
        heappush(self.container, (cost, path))
        print(f"+ {path_string(path)}, {cost} # {cost - head_estimate} + {head_estimate} = {cost}")
        
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
    graph = AStarGraph(
        nodes={'A', 'B', 'C', 'D', 'G'},
        estimates={'A':5, 'B':5, 'C':9, 'D':1, 'G':0},
        edge_list=[('A','B',2), ('A','C',3), ('B','D',5), ('C','D',10), ('D','G',3)],
        starting_nodes=['A'],
        goal_nodes={'G'},
        )
    solution = next(generic_search(graph, AStarFrontier()))
    print_actions(solution)
    
    s = 's'
    a = 'a'
    b = 'b'
    g = 'g'
    graph = AStarGraph(
        nodes={s, a, b, g},
        estimates = {s:7, a:2, b:6, g:0},
        edge_list=[(s,a,3), (s,b,1),
         (b,a,1), (a,g,5)],
        starting_nodes = [s],
        goal_nodes = {g}
        )
    solution = next(generic_search(graph, AStarFrontier()))
    print_actions(solution)
    
    graph = AStarGraph(
        nodes={'A', 'B', 'C', 'D', 'G'},
        estimates={'A':10, 'B':1, 'C':1, 'D':8, 'G':0},
        edge_list=[('A','B',1), ('B','C',1), ('C','B',1), ('B','D',10), ('D','G',9)],
        starting_nodes=['A'],
        goal_nodes={'G'}
        )
    solution = next(generic_search(graph, AStarFrontier()))
    print_actions(solution)        

if __name__ == '__main__':
    main()