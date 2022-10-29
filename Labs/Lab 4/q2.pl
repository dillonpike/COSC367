reflection(point(X, Y), point(Y, X)).

test_answer :-
	reflection(point(-5, 8), point(X, Y)),
        writeln(point(X, Y)).
