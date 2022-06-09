from itertools import combinations
import random

def n_queens_neighbours(state):
    neighbours = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i < j:
                state_list = list(state)
                state_list[i], state_list[j] = state_list[j], state_list[i]
                neighbours.append(tuple(state_list))
    return sorted(neighbours)

def n_queens_cost(state):
    return len([x1 for (x1, y1), (x2, y2) in combinations(enumerate(state), 2) 
                if abs(x1-x2) == abs(y1-y2)])


def greedy_descent(initial_state, neighbours, cost):
    path = [initial_state]
    while len(n := neighbours(initial_state)) > 0:
        min_neighbour = min(n, key=cost)
        if cost(min_neighbour) < cost(initial_state):
            path.append(min_neighbour)
            initial_state = min_neighbour
        else:
            return path
    return path

def greedy_descent_recursive(initial_state, neighbours, cost):
    neighbour_list = neighbours(initial_state)
    if len(neighbour_list) == 0:
        return [initial_state]
    min_neighbour = min(neighbour_list, key=cost)
    if cost(min_neighbour) < cost(initial_state):
        return [initial_state] + greedy_descent(min_neighbour, neighbours, cost)
    else:
        return [initial_state]
    
def greedy_descent_with_random_restart(random_state, neighbours, cost):
    while True:
        initial_state = random_state()
        path = greedy_descent(initial_state, neighbours, cost)
        for state in path:
            print(state)
        if cost(path[-1]) != 0:
            print("RESTART")
        else:
            break

def main():
    def cost(x):
        return x**2
    
    def neighbours(x):
        return [x - 1, x + 1]
    
    for state in greedy_descent(4, neighbours, cost):
        print(state)
    
    for state in greedy_descent(-6.75, neighbours, cost):
        print(state)
        
    def cost(x):
        return -x**2
    
    def neighbours(x):
        return [x - 1, x + 1] if abs(x) < 5 else []
    
    for state in greedy_descent(0, neighbours, cost):
        print(state)
        
    N = 6
    random.seed(0)
    
    def random_state():
        return tuple(random.sample(range(1,N+1), N))   
    
    greedy_descent_with_random_restart(random_state, n_queens_neighbours , n_queens_cost)
    
    N = 8
    random.seed(0)

    def random_state():
        return tuple(random.sample(range(1,N+1), N))   
    
    greedy_descent_with_random_restart(random_state, n_queens_neighbours , n_queens_cost)    
    
if __name__ == '__main__':
    main()