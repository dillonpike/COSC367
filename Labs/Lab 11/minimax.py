def terminal_test(tree):
    return type(tree) == int

def max_value(tree):
    if terminal_test(tree):
        return tree
    else:
        return max(min_value(child) for child in tree)

def min_value(tree):
    if terminal_test(tree):
        return tree
    else:
        return min(max_value(child) for child in tree)
    
def max_action_value(game_tree):
    if terminal_test(game_tree):
        return None, game_tree
    else:
        utility = max_value(game_tree)
        for action, child in enumerate(game_tree):
            if min_value(child) == utility:
                return action, utility

def min_action_value(game_tree):
    if terminal_test(game_tree):
        return None, game_tree
    else:
        utility = min_value(game_tree)
        for action, child in enumerate(game_tree):
            if max_value(child) == utility:
                return action, utility

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
    
    game_tree = [2, [-3, 1], 4, 1]
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
    game_tree = 3
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
    game_tree = [1, 2, [3]]
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
    
    game_tree = [1, 2, [[-3, 3]]]
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)    
    
if __name__ == '__main__':
    main()