from search import *
from collections import deque

class BFSFrontier(Frontier):
    
    def __init__(self):
        self.container = deque()
    
    def add(self, path):
        self.container.append(path)
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration

class FunkyNumericGraph(Graph):
    
    def __init__(self, starting_number):
        self.starting_number = starting_number
    
    def is_goal(self, node):
        return node % 10 == 0
    
    def starting_nodes(self):
        return [self.starting_number]
    
    def outgoing_arcs(self, tail_node):
        return [Arc(tail_node, tail_node-1, action="1down", cost=1),
                Arc(tail_node, tail_node+2, action="2up", cost=1)]
            
            
            
def main():
    graph = FunkyNumericGraph(4)
    for node in graph.starting_nodes():
        print(node)

    graph = FunkyNumericGraph(4)
    for arc in graph.outgoing_arcs(7):
        print(arc)
    
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    print()
    print_actions(next(solutions))
    
    from itertools import dropwhile 
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))

if __name__ == '__main__':
    main()