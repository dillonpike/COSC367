from search import *
from heapq import *
import math

class RoutingGraph(Graph):
    def __init__(self, map_string):
        self.map_list = map_string.splitlines()
        rows = len(self.map_list)
        cols = len(self.map_list[0])
        self.goals = [(row, col) for row in range(rows) for col in range(cols)
                      if self.map_list[row][col] == 'G']
        self.tile_cost = 5
    
    def starting_nodes(self):
        rows = len(self.map_list)
        cols = len(self.map_list[0])
        nodes = []
        for i in range(rows):
            for j in range(cols):
                if self.map_list[i][j] == 'S':
                    nodes.append((i, j, math.inf))
                elif self.map_list[i][j].isdigit():
                    nodes.append((i, j, int(self.map_list[i][j])))
        return nodes
                
    def is_goal(self, node):
        row, col, fuel = node
        return self.map_list[row][col] == 'G'
                
    def outgoing_arcs(self, node):
        rows = len(self.map_list)
        cols = len(self.map_list[0])
        
        row, col, fuel = node
        arcs = []
        
        if fuel > 0:
            if self.map_list[row-1][col] not in ['-', 'X']:
                new_node = (row-1, col, fuel-1)
                arcs.append(Arc(node, new_node, 'N', self.tile_cost))
            if self.map_list[row][col+1] not in ['|', 'X']:
                new_node = (row, col+1, fuel-1)
                arcs.append(Arc(node, new_node, 'E', self.tile_cost))
            if self.map_list[row+1][col] not in ['-', 'X']:
                new_node = (row+1, col, fuel-1)
                arcs.append(Arc(node, new_node, 'S', self.tile_cost))
            if self.map_list[row][col-1] not in ['|', 'X']:
                new_node = (row, col-1, fuel-1)
                arcs.append(Arc(node, new_node, 'W', self.tile_cost))
        if self.map_list[row][col] == 'F' and fuel < 9:
            new_node = (row, col, 9)
            arcs.append(Arc(node, new_node, 'Fuel up', 15))            
        return arcs
    
    def estimated_cost_to_goal(self, node):
        row, col, fuel = node
        cost = math.inf
        for goal_row, goal_col in self.goals:
            new_cost = self.tile_cost*(abs(row - goal_row) + abs(col - goal_col))
            if new_cost < cost:
                cost = new_cost
        return cost
    
class AStarFrontier(Frontier):
    
    def __init__(self, graph):
        self.graph = graph
        self.container = []
        self.expanded = set()
        self.entry_count = 0
    
    def add(self, path):
        if path[-1].head not in self.expanded:
            cost = sum(arc.cost for arc in path) + self.graph.estimated_cost_to_goal(path[-1].head)
            heappush(self.container, (cost, self.entry_count, path))
            self.entry_count += 1
        
    def __next__(self):
        while True:
            if len(self.container) > 0:
                popped = heappop(self.container)
                if popped[2][-1].head not in self.expanded:
                    self.expanded |= {popped[2][-1].head}
                    return popped[2]
            else:
                raise StopIteration
            
def print_map(graph, frontier, solution):
    """
    Parameters: instance of RoutingGraph, a frontier object, and a solution 
    (which is a sequence of Arc objects that make up a path from a starting 
    position to the goal position).
    """
    map_list = graph.map_list
    map_list = list(map(list, map_list))
    expanded = frontier.expanded
    for row, col, fuel in expanded:
        if map_list[row][col] == ' ':
            map_list[row][col] = '.'
    if solution is not None:
        for arc in solution:
            row, col, fuel = arc.head
            if map_list[row][col] == '.':
                map_list[row][col] = '*'
    for row in map_list:
        print(''.join(row))

def main():
    map_str = """\
+----------+
|    X    G|
| S  X     |
|    X  G  |
+----------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution) 

    map_str = """\
+-------+
|   G   |
|       |
|   S   |
+-------+
"""

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    map_str = """\
+-------+
|  GG   |
|S    G |
|  S    |
+-------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    map_str = """\
+-------+
|     XG|
|X XXX  |
| S     |
+-------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    map_str = """\
+-------+
|  F  X |
|X XXXXG|
| 3     |
+-------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    map_str = """\
+--+
|GS|
+--+
"""
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    map_str = """\
+---+
|GF2|
+---+
"""
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    map_str = """\
+----+
| S  |
| SX |
|GX G|
+----+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)    
    
    map_str = """\
+---------+
|    X    |
|   XGX   |
|    X  S |
+---------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    
    map_str = """\
+----------------+
|2              F|
|XX     G 123    |
|3XXXXXXXXXXXXXX |
|  F             |
|          F     |
+----------------+
""" # tests stability
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|                |
|                |
|     G          |
|                |
|                |
|                |
+----------------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|                |
|                |
|     G          |
|                |
|                |
|                |
+----------------+
"""
    
    
    map_graph = RoutingGraph(map_str)
    # changing the heuristic so the search behaves like LCFS
    map_graph.estimated_cost_to_goal = lambda node: 0
    
    frontier = AStarFrontier(map_graph)
    
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
+-------------+
| G         G |
|      S      |
| G         G |
+-------------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
+-------+
|     XG|
|X XXX  |
|  S    |
+-------+
"""
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
+--+
|GS|
+--+
"""
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
+----+
|    |
| SX |
| X G|
+----+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
+---------------+
|    G          |
|XXXXXXXXXXXX   |
|           X   |
|  XXXXXX   X   |
|  X S  X   X   |
|  X        X   |
|  XXXXXXXXXX   |
|               |
+---------------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
+------------+
|         X  |
| S       X G|
|         X  |
|         X  |
|         X  |
+------------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    
    map_str = """\
+-------------+
|    XG       |
|    XXXXX  X |
|S        X   |
+-------------+
"""
    
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

if __name__ == '__main__':
    main()