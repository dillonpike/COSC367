from search import *
from statistics import pvariance
from heapq import *


class PriorityFrontier(Frontier):
    

    def __init__(self):
        # The constructor does not take any arguments.
        self.container = []
        # Complete the rest
        self.entry_count = 0
        self.expanded = set()
        

    def add(self, path):
        #raise NotImplementedError # FIX THIS: Replace it with proper code
        costs = [arc.cost for arc in path]
        variance = pvariance(costs)
        if path[-1].head not in self.expanded:
            heappush(self.container, (sum(costs), variance, self.entry_count, path))
            self.entry_count += 1

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional information for iteration."""
        return self
        
    def __next__(self):
        # Complete
        #raise StopIteration   # raise this when the container is exhuasted
        while True:
            if len(self.container) > 0:
                popped = heappop(self.container)
                if popped[-1][-1].head not in self.expanded:
                    self.expanded |= {popped[-1][-1].head}
                    return popped[-1]
            else:
                raise StopIteration        
    

def main(): 
    graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

    solution = next(generic_search(graph, PriorityFrontier()))
    print_actions(solution)
    
    graph = ExplicitGraph(
        nodes = {'S', 'A', 'B', 'G'},
        edge_list=[('S','A', 1), ('S','B',2),
                   ('A', 'G', 3), ('B', 'G', 2)],
        starting_nodes = ['S'],
        goal_nodes = {'G'})
    
    solution = next(generic_search(graph, PriorityFrontier()))
    print_actions(solution)   
    
    graph = ExplicitGraph(
        nodes = {'S', 'A', 'B', 'C', 'G', 'F'},
        edge_list=[('S','A', 1), ('C', 'S', 2), ('S','C',2), ('S', 'B', 2),
                   ('A', 'G', 3), ('C', 'G', 2), ('B', 'G', 2)],
        starting_nodes = ['S'],
        goal_nodes = {'F'})
    
    solution = next(generic_search(graph, PriorityFrontier()), None)
    print_actions(solution)
    
    graph = ExplicitGraph(
        nodes = {'S', 'A', 'B', 'G'},
        edge_list=[('S','A', 1), ('A', 'B', 1), ('B','S',1)],
        starting_nodes = ['S'],
        goal_nodes = {'G'})
    
    solution = next(generic_search(graph, PriorityFrontier()), None)
    print_actions(solution)    

if __name__ == '__main__':
    main()
