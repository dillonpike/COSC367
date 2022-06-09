from search import *
from collections import deque

class BFSFrontier(Frontier):
    
    def __init__(self):
        self.container = deque()
    
    def add(self, path):
        self.container.append(path)
        print(f" + {path_string(path)}")
        
    def __next__(self):
        if len(self.container) > 0:
            popped = self.container.popleft()
            print(f" - {path_string(popped)}")            
            return popped
        else:
            raise StopIteration
        
def path_string(path):
    path_string = ''
    for arc in path:
        path_string += arc.head
    return path_string
        
def main(): 
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list = [('S','A'), ('S', 'G'), ('A', 'G')],
                          starting_nodes = ['S'],
                          goal_nodes = {'G'})
    
    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    
    
    flights = ExplicitGraph(nodes=['Christchurch', 'Auckland', 
                               'Wellington', 'Gold Coast'],
                        edge_list = [('Christchurch', 'Gold Coast'),
                                 ('Christchurch','Auckland'),
                                 ('Christchurch','Wellington'),
                                 ('Wellington', 'Gold Coast'),
                                 ('Wellington', 'Auckland'),
                                 ('Auckland', 'Gold Coast')],
                        starting_nodes = ['Christchurch'],
                        goal_nodes = {'Gold Coast'})

    my_itinerary = next(generic_search(flights, BFSFrontier()), None)
    print_actions(my_itinerary)
    
    graph = ExplicitGraph(
        nodes={'G', 'E', 'H', 'B'},
        edge_list=[('E', 'G'), ('H', 'B'), ('G','B'), ('H','G')],
        starting_nodes=['H'],
        goal_nodes={'E'}
    )
    
    print_actions(next(generic_search(graph, BFSFrontier()), None))
    
    graph = ExplicitGraph(
        nodes={'A', 'B', 'C', 'D'},
        edge_list=[('B', 'A'), ('C', 'D'), ('A','D'), ('C','A')],
        starting_nodes=['C'],
        goal_nodes={'B'},
    )
    
    print_actions(next(generic_search(graph, BFSFrontier()), None))
    
if __name__ == '__main__':
    main()