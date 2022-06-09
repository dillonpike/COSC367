def unnest(alist):
    blist = []
    for i in range(len(alist)):
        if type(alist[i]) != list:
            blist.append(alist[i])
        else:
            blist.extend(unnest(alist[i]))
    return blist

def num_crossovers(parent_expression1, parent_expression2):
    if type(parent_expression1) != list:
        length1 = 1
    else:
        length1 = len(unnest(parent_expression1))
    if type(parent_expression2) != list:
        length2 = 1
    else:
        length2 = len(unnest(parent_expression2))
    return length1 * length2
    
def main():
    expression1 = ['+', 12, 'x']
    expression2 = ['-', 3, 6]
    print(num_crossovers(expression1, expression2))
    
    expression1 = 'weight'
    expression2 = ['-', 8, 4]
    print(num_crossovers(expression1, expression2))
    
    expression1 = 'weight'
    expression2 = 'bruh'
    print(num_crossovers(expression1, expression2))
    
    expression1 = ['add', ['add', 22, 'y'], 'x']
    expression2 = ['add', ['b', ['c', ['c', 1, 2], 2], '2'], 'x']
    print(num_crossovers(expression1, expression2))
    
    
if __name__ == '__main__':
    main()
    