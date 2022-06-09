from search import *
from collections import deque
import copy

BLANK = ' '

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
        
class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""
        
        n = len(state) # the size of the puzzle
        i, j = next((i, j) for i in range(n) for j in range(n)
                    if state[i][j] == BLANK) # find the blank tile
        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i-1][j]) # or blank goes up
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i+1][j]) # or blank goes down
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j-1]) # or blank goes left
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j+1]) # or blank goes right
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]
    
    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""
        
        n = len(state)
        current = -1
        if state[0][0] != ' ':
            return False        
        for i in range(n):
            for j in range(n):
                if (i, j) != (0, 0) and state[i][j] != current + 1:
                    return False
                else:
                    current += 1
        return True

def main():
    graph = SlidingPuzzleGraph([[1, 2, 5],
                                [3, 4, 8],
                                [6, 7, ' ']])
    
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    
    graph = SlidingPuzzleGraph([[3,' '],
                                [1, 2]])
    
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    
    graph = SlidingPuzzleGraph([[1, ' ', 2],
                                [6,  4,  3],
                                [7,  8,  5]])
    
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    
if __name__ == '__main__':
    main()