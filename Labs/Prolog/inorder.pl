inorder(leaf(X), [X]).
inorder(tree(Root, Left, Right), L2) :-
        inorder(Left, LeftL),
        inorder(Right, RightL),
        append(LeftL, [Root], L1),
        append(L1, RightL, L2).
        
test_answer1 :- inorder(tree(1, leaf(2), leaf(3)), T), writeln(T).
test_answer2 :- inorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).