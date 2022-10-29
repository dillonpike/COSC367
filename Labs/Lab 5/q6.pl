split_odd_even([], [], []).
split_odd_even([X], [X], []).
split_odd_even([X,Y|InTail], [X|OutA], [Y|OutB]) :- split_odd_even(InTail, OutA, OutB).

test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).

test_answer2 :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).
