import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
        
def forward_deduce(knowledge_base):
    clause_list = list(clauses(knowledge_base))
    true_atoms = set()
    change = True
    while change:
        change = False
        for clause in clause_list:
            if clause[0] not in true_atoms and all(atom in true_atoms for atom in clause[1]):
                true_atoms |= {clause[0]}
                change = True
    return true_atoms
        
def main():
    kb = """
    a :- b.
    b.
    """
    
    print(", ".join(sorted(forward_deduce(kb))))
    
    kb = """
    good_programmer :- correct_code.
    correct_code :- good_programmer.
    """
    
    print(", ".join(sorted(forward_deduce(kb))))
    
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
    
    print(", ".join(sorted(forward_deduce(kb))))
    
if __name__ == '__main__':
    main()