def max_value(tree):
    if type(tree) == int:
        return tree
    else:
        return max(min_value(child) for child in tree)

def min_value(tree):
    if type(tree) == int:
        return tree
    else:
        return min(max_value(child) for child in tree)

def main():
    game_tree = 3
    
    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))
    
    game_tree = [1, 2, 3]
    
    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))
    
    game_tree = [1, 2, [3]]
    
    print(min_value(game_tree))
    print(max_value(game_tree))

    game_tree = [[1, 2], [3]]
    
    print(min_value(game_tree))
    print(max_value(game_tree))
    
if __name__ == '__main__':
    main()