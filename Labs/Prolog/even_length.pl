even_length([]).
even_length([H1,H2|T]) :- even_length(T).

test_answer1 :-
    even_length([foo, bar, zoo, log]),
    writeln('OK').

test_answer2 :-
    \+ even_length([1]),
    \+ even_length(this_is_not_a_list),
    writeln('OK').

