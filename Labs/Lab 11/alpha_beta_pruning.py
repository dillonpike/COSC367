def terminal_test(tree):
    return type(tree) == int

def max_value(tree, alpha, beta):
    if terminal_test(tree):
        return tree
    else:
        value = -float('inf')
        for i, child in enumerate(tree):
            value = max(value, min_value(child, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                tree[:] = tree[:i+1]
                print(f"({alpha}, {beta})")
                return value
        return value

def min_value(tree, alpha, beta):
    if terminal_test(tree):
        return tree
    else:
        value = float('inf')
        for i, child in enumerate(tree):
            value = min(value, max_value(child, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                tree[:] = tree[:i+1]
                print(f"({alpha}, {beta})")
                return value
        return value
    
def max_alpha_beta_search(game_tree):
    if terminal_test(game_tree):
        return None, game_tree
    else:
        utility = max_value(game_tree, -float('inf'), float('inf'))
        for action, child in enumerate(game_tree):
            if min_value(child, -float('inf'), float('inf')) == utility:
                return action, utility

        
def min_alpha_beta_search(game_tree):
    if terminal_test(game_tree):
        return None, game_tree
    else:
        utility = min_value(game_tree, -float('inf'), float('inf'))
        for action, child in enumerate(game_tree):
            if max_value(child, -float('inf'), float('inf')) == utility:
                return action, utility
        
def main():

    game_tree = [2, [-1, 5], [1, 3], 4]
    action, value = max_alpha_beta_search(game_tree)
    print("Pruned tree:", game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
    game_tree = [0, [-2, 1], 5]
    action, value = min_alpha_beta_search(game_tree)
    print("Pruned tree:", game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
    game_tree = [3, [[2, 1], [4, [7, -2]]], 0]
    action, value = max_alpha_beta_search(game_tree)
    print("Pruned tree:", game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
    game_tree = [[-1, [7 , 16], 16], [7, -5, 2]]
    action, value = max_alpha_beta_search(game_tree)
    print("Pruned tree:", game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value) 
    
if __name__ == '__main__':
    main()
