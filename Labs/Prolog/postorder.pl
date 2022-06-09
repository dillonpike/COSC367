postorder(leaf(X), [X]).
postorder(tree(Root, Left, Right), L2) :-
        postorder(Left, LeftL),
        postorder(Right, RightL),
        append(LeftL, RightL, L1),
        append(L1, [Root], L2).



test_answer1 :- postorder(tree(a, leaf(b), leaf(c)), T), writeln(T).

test_answer2 :- postorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).