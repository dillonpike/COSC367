import re
from search import *


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        return [atom for atom in self.query]
        
    def is_goal(self, node):
        return node == []

    def outgoing_arcs(self, tail_node):
        arcs = []
        if type(tail_node) is not list:
            tail_node = [tail_node]
        for i in range(len(tail_node)):
            for clause in self.clauses:
                if tail_node[i] == clause[0]:
                    head = tail_node[:i] + clause[1] + tail_node[i+1:]
                    arcs.append(Arc(tail_node, head, str(tail_node) + '->' + str(head), 1))
        return arcs

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first                                                                                                                                                                         
    search."""
    def __init__(self):
        self.container = []
    
    def add(self, path):
        self.container.append(path)
        #print(f" + {path_string(path)}")
        
    def __next__(self):

        if len(self.container) > 0:
            popped = self.container.pop()
            #print(f" - {path_string(popped)}")
            return popped
        else:
            raise StopIteration
        
def main():
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """
    
    query = {'a'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")
        
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """
    
    query = {'a', 'b', 'd'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")
        
        kb = """
        all_tests_passed :- program_is_correct.
        all_tests_passed.
        """
        
    query = {'program_is_correct'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")
        
        kb = """
        a :- b.
        """
        
        query = {'c'}
        if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
            print("The query is true.")
        else:
            print("The query is not provable.")    

if __name__ == '__main__':
    main()