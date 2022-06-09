asbs([]).
asbs([a|T]) :- as([H|T]).
asbs([b|T]) :- bs([H|T]).
as([]).
as([a|T]) :- as(T).
as([b|T]) :- bs(T).
bs([]).
bs([b|T]) :- bs(T).

test_answer1 :-
    asbs([a,a,a,b]),
    writeln('OK').

test_answer2 :-
    \+ asbs([a,b,a]),
    writeln('OK').

