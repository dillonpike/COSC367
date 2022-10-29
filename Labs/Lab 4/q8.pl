mirror(leaf(X), leaf(X)).
mirror(tree(X1, Y1), tree(Y2, X2)) :-
        mirror(X1, X2),
        mirror(Y1, Y2).


test_answer :-
    mirror(tree(tree(leaf(1),  leaf(2)),  tree(leaf(3), leaf(4))), T),
    write(T),
    halt.

test_answer :-
    write('Wrong answer!'),
    halt.
