same_evens([]).
same_evens([H1,H2|[]]).
same_evens([H1,H2|T]) :- same_evens_helper(T, H2).

same_evens_helper([], H2).
same_evens_helper([H1,H2|[]], H2).
same_evens_helper([H1,H2|T], H2) :- same_evens_helper(T, H2).

test_answer1 :-
    same_evens([a, b, c, b, d, b]),
    same_evens([a, b]),
    same_evens([]),
    writeln('OK').

test_answer2 :-
    \+ same_evens([2]),
    \+ same_evens(this_is_not_a_list),
    \+ same_evens([a, b, a, c]),
    writeln('OK').

test_answer2 :-
    writeln('Wrong!').
