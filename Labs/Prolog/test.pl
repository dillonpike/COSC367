product(_, [], []).
product(X, [H|T], [(X,H)|XcrossB]) :- product(X, T, XcrossB).
cartesian_product([], _, []).
cartesian_product([H|T], B, AcrossB) :- product(H, B, XcrossB), 
                                        cartesian_product(T, B, TcrossB),
                                        append(XcrossB, TcrossB, AcrossB).

test_answer1 :- cartesian_product([a, b], [1, 2], X),
               writeln(X).

test_answer2 :- cartesian_product([a, b], X, 
                                 [(a,1), (a,2), (b,1), (b,2)]),
               writeln(X).