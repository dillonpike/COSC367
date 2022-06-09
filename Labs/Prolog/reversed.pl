append([], L, L).
append([H|L1], L2, [H|L3]) :- append(L1, L2, L3).

reversed([], []).
reversed([Head|Tail], Backward) :- 
        reversed(Tail, ReversedTail),
        append(ReversedTail, [Head], Backward).

test_answer1 :- 
    reversed([1, 2, 3, 4, 5], L),
    writeln(L).

test_answer2 :- 
    reversed(L, [d, c, b, a]),
    writeln(L).