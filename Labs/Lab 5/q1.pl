second([_,X|Tail], X).

test_answer :-
    \+ second([1], X),
    writeln('OK').

test_answer :-
    second([_],_),
    writeln('The predicate should fail on lists of length one!').
