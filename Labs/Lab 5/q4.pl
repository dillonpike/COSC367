twice([], []).
twice([E1|InTail], [E1,E1|OutTail]) :- twice(InTail, OutTail).


test_answer :-
    twice([a, b, c, d], L),
    writeln(L).
