append([], L, L).
append([H|L1], L2, [H|L3]) :- append(L1, L2, L3).

preorder(leaf(X), [X]).
preorder(tree(Root, Left, Right), L3) :-
        preorder(Left, LTraversal),
        preorder(Right, RTraversal),
        append([Root|LTraversal], RTraversal, L3).

test_answer :- preorder(leaf(a), L),
               writeln(L).

test_answer2 :- preorder(tree(a, tree(b, leaf(c), tree(pee, leaf(piss), leaf(poo))), leaf(e)), T),
               writeln(T).
