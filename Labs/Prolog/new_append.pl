new_append([], L, L).
new_append([Head|Tail], L, [Head|L2]) :- new_append(Tail, L, L2).

test_answer1 :-
    new_append([1, 2, 3], [a, b, c], L),
    writeln(L).

test_answer2 :-
    new_append([1, 2, 3], L, [1, 2, 3, 4, 5]),
    writeln(L).