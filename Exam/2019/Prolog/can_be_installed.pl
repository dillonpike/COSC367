is_installed([]).
is_installed([H|T]) :- installed(L), member(H, L), is_installed(T).
can_be_installed(X) :- requires(X, L), is_installed(L).

requires(prolog, [cmake, yaml, ncurses]).

installed([cmake, java]).
installed([yaml, json]).
installed([vim, emacs]).
installed([ncurses]).

test_answer1 :- 
    can_be_installed(prolog),
    writeln("OK").

test_answer1 :-
    \+ can_be_installed(prolog),
    writeln("Wrong!").
    
    
requires(learn, [php, sql]).

installed([php, gcc]).

test_answer2 :- 
    \+ can_be_installed(learn),
    writeln("OK").

test_answer2 :-
    can_be_installed(learn),
    writeln("Wrong!").