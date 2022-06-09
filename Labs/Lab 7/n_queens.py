from itertools import combinations

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
                
def main():
    print(n_queens_neighbours((1, 2)))
    print(n_queens_neighbours((1, 3, 2)))
    print(n_queens_neighbours((1, 2, 3)))
    print(n_queens_neighbours((1,)))
    for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
        print(neighbour)
    for neighbour in n_queens_neighbours((2, 3, 1, 4)):
        print(neighbour)
        
    print(n_queens_cost((1, 2)))
    print(n_queens_cost((1, 3, 2)))
    print(n_queens_cost((1, 2, 3)))
    print(n_queens_cost((1,)))
    print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))
    print(n_queens_cost((2, 3, 1, 4)))

if __name__ == '__main__':
    main()