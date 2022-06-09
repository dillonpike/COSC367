import itertools, copy 
from csp import *

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c): # COMPLETE
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime): # COMPLETE
                        if x != z: # COMPLETE
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp

def main():
    simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
        })

    csp = arc_consistent(simple_csp)
    for var in sorted(csp.var_domains.keys()):
        print("{}: {}".format(var, sorted(csp.var_domains[var])))
        
    csp = CSP(var_domains={x:set(range(10)) for x in 'abc'},
              constraints={lambda a,b,c: 2*a+b+2*c==10}) 
    
    csp = arc_consistent(csp)
    for var in sorted(csp.var_domains.keys()):
        print("{}: {}".format(var, sorted(csp.var_domains[var])))
        
    crossword_puzzle = CSP(
        var_domains={
            # read across:
            'a1': set("bus has".split()),
            'a3': set("lane year".split()),
            'a4': set("ant car".split()),
            # read down:
            'd1': set("buys hold".split()),
            'd2': set("search syntax".split()),
            },
        constraints={
            lambda a1, d1: a1[0] == d1[0],
            lambda d1, a3: d1[2] == a3[0],
            lambda a1, d2: a1[2] == d2[0],
            lambda d2, a3: d2[2] == a3[2],
            lambda d2, a4: d2[4] == a4[0],
            })
    
    crossword_puzzle = arc_consistent(crossword_puzzle)
    for var in sorted(crossword_puzzle.var_domains.keys()):
        print("{}: {}".format(var, sorted(crossword_puzzle.var_domains[var])))
        
    canterbury_colouring = CSP(
        var_domains={
            'christchurch': {'red', 'green'},
            'selwyn': {'red', 'green'},
            'waimakariri': {'red', 'green'},
            },
        constraints={
            lambda christchurch, waimakariri: christchurch != waimakariri,
            lambda christchurch, selwyn: christchurch != selwyn,
            lambda selwyn, waimakariri: selwyn != waimakariri,
            })
    
    canterbury_colouring = arc_consistent(canterbury_colouring)
    for var in sorted(canterbury_colouring.var_domains.keys()):
        print("{}: {}".format(var, sorted(canterbury_colouring.var_domains[var]))) 

if __name__ == '__main__':
    main()