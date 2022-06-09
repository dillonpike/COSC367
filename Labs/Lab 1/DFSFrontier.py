from search import *

class DFSFrontier(Frontier):
    
    def __init__(self):
        self.container = []
    
    def add(self, path):
        self.container.append(path)
        print(f" + {path_string(path)}")
        
    def __next__(self):

        if len(self.container) > 0:
            popped = self.container.pop()
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
    available_flights = ExplicitGraph(
        nodes=['Christchurch', 'Auckland', 
               'Wellington', 'Gold Coast'],
        edge_list=[('Christchurch', 'Gold Coast'),
                   ('Christchurch','Auckland'),
                   ('Christchurch','Wellington'),
                   ('Wellington', 'Gold Coast'),
                   ('Wellington', 'Auckland'),
                   ('Auckland', 'Gold Coast')],
        starting_nodes=['Christchurch'],
        goal_nodes={'Gold Coast'})
    
    my_itinerary = next(generic_search(available_flights, DFSFrontier()), None)
    print_actions(my_itinerary)
    
    graph= ExplicitGraph(
        nodes={'S', 'A', 'B', 'G'},
        edge_list=[('A', 'B', 5), ('S', 'G', 7), ('S', 'A', 6), ('B', 'G', 10)],
        starting_nodes=['S'],
        goal_nodes={'G'}
    )
    
    graph= ExplicitGraph(
        nodes={'S', 'A', 'B', 'G'},
        edge_list=[('S', 'A'), ('A', 'B'), ('B', 'A'), ('S', 'G')],
        starting_nodes=['S'],
        goal_nodes={'G'}
    )    
    
    print_actions(next(generic_search(graph, DFSFrontier()), None))
    
    graph = ExplicitGraph(
        nodes={'A', 'B', 'C', 'G'},
        edge_list=[('A', 'B'), ('A', 'G'), ('B', 'C'), ('C', 'A'), ('C', 'G')],
        starting_nodes=['A', 'B'],
        goal_nodes={'G'}
    )
    
    print_actions(next(generic_search(graph, DFSFrontier()), None))
    
    
if __name__ == '__main__':
    main()