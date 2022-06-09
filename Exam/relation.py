import itertools, copy 
from csp import *

def get_relations(csp):
    """Returns the relations of the csp."""
    relations = []
    for constraint in csp.constraints:
        header = sorted(scope(constraint))
        tuples = set()
        for tup in itertools.product(*[csp.var_domains[var] for var in header]):
            assignment = ({var: val for var, val in zip(header, tup)})
            if satisfies(assignment, constraint):
                tuples.add(tup)
        relations.append(Relation(header, tuples))
    return relations

def eliminate_variable(relations, to_remove):
    """Joins relations through common variables and removes the to_remove
       variable from the joined relation.
    """
    to_join = [relation for relation in relations if to_remove in relation.header]
    to_not_join = [relation for relation in relations if to_remove not in relation.header]
    header = sorted(set(var for relation in to_join for var in relation.header) - {to_remove})
    common_vars = set(to_join[0].header)
    for relation in to_join:
        common_vars &= set(relation.header)
    common_vars = list(common_vars)
    relation_tuples = [relation.tuples for relation in to_join]
    joined_tuples = set()
    for product in itertools.product(relation_tuples[0], *relation_tuples[1:]):
        assignments = []
        for i in range(len(product)):
            assignments.append({var: val for var, val in zip(to_join[i].header, product[i])})
        i = 1
        can_join = True
        while i < len(assignments) and can_join is True:
            for var in common_vars:
                if assignments[i-1][var] != assignments[i][var]:
                    can_join = False
                    break
            i += 1
        if can_join:
            joined_assignment = assignments[0]
            for i in range(1, len(assignments)):
                joined_assignment.update(assignments[i])
            joined_assignment.pop(to_remove)
            joined_tuples.add(tuple(joined_assignment[var] for var in header))
    joined = Relation(header, joined_tuples)
    return to_not_join + [joined]
        
def main():
    csp = CSP(
        var_domains = {var:{0,1,2} for var in 'abcd'},
        constraints = {
            lambda a, b, c: a > b + c,
            lambda c, d: c > d
        }
    )
    print(get_relations(csp))
    
    csp = CSP(
        var_domains = {var:{-1,0,1} for var in 'abcd'},
        constraints = {
           lambda a, b: a == abs(b),
           lambda c, d: c > d,
           lambda a, b, c: a * b > c + 1
        }
    )
    relations = get_relations(csp)
    print(f"relations = {relations}")
    relations = eliminate_variable(relations, 'a')
    print(f"relations_after_elimination = {relations}")
    
    csp = CSP(
        var_domains = {var:{-1,0,1} for var in 'abc'},
        constraints = {
            lambda a, b: a * b == -1,
            lambda b, c: b + c == 1,
        }
    )
    relations = get_relations(csp)
    print(relations)
    relations = eliminate_variable(relations, 'b')
    print(relations)
    
    csp = CSP(
        var_domains = {var:{-1,0,1} for var in 'abc'},
        constraints = {
            lambda a, b: a * b > 0,
            lambda b, c: b + c > 0,
        }    
    )
    relations = get_relations(csp)
    print(relations)
    relations = eliminate_variable(relations, 'b')
    print(relations)
    
    csp = CSP(
        var_domains = {var:{-1,0,1} for var in 'abc'},
        constraints = {
            lambda a, b: a * b > 0,
            lambda a: a > 0,
        }    
    )
    relations = get_relations(csp)
    print(relations)
    relations = eliminate_variable(relations, 'a')
    print(relations)
    
    csp = CSP(
       var_domains = {var:{1,2,3,4} for var in 'abc'},
       constraints = {
          lambda a, b, c: a < b < c,
          lambda b: b % 2 == 0,
          }
        )
    relations = get_relations(csp)
    print(relations)
    relations = eliminate_variable(relations, 'b')
    print(relations)    
    

if __name__ == '__main__':
    main()