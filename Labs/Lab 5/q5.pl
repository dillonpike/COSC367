remove(X, [], []).
remove(X, [X|InT], OutT) :- remove(X, InT, OutT).
remove(X, [Y|InT], [Y|OutT]) :- remove(X, InT, OutT).

test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).

test_answer2 :-
    remove(2, [2], L),
    writeln(L).

test_answer3 :-
    remove(d, [a, b, c], L),
    write(L).

test_answer4 :-
    remove(a, [], L),
    write(L).

test_answer5 :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').
