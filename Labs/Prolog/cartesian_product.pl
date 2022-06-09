cartesian_helper(_, [], []).
cartesian_helper(X, [H|T], [(X,H)|XcrossB]) :- cartesian_helper(X, T, XcrossB).

cartesian_product([], _, []).
cartesian_product([HA|TA], B, AcrossB) :- 
        cartesian_helper(HA, B, HAcrossB),
        cartesian_product(TA, B, TAcrossB),
        append(HAcrossB, TAcrossB, AcrossB).


test_answer1 :- cartesian_product([a, b], [1, 2], X),
               writeln(X).

test_answer2 :- cartesian_product([a, b], X, 
                                 [(a,1), (a,2), (b,1), (b,2)]),
               writeln(X).

test_answer3 :- cartesian_product([a, b, c], [], X),
               writeln(X),
               cartesian_product([], [a, b, c], Y),
               writeln(Y).