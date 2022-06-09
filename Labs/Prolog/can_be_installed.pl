is_installed([]).
is_installed([H|T]) :- installed(L), member(H, L), is_installed(T).
can_be_installed(X) :- requires(X, L), is_installed(L).
                       

requires(learn, [php, sql]).

installed([php, gcc]).

test_answer :- 
    \+ can_be_installed(learn),
    writeln("OK").

test_answer :-
    can_be_installed(learn),
    writeln("Wrong!").