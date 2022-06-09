% My past solution
% has_cycle([H|T]) :- member(H, T).
% has_cycle([H|T]) :- has_cycle(T).

contains(X, [H|T]) :- (X=H); contains(X, T).
has_cycle([H|T]) :- contains(H, T); has_cycle(T).

test_answer1 :-
    has_cycle([a,b,c,d,a,e,f]),
    writeln('OK').

test_answer1 :-
    writeln('Wrong!').
    
% Note: \+ means 'not'

test_answer2 :-
    \+ has_cycle([a,b,c,d,e,f]),
    writeln('OK').

test_answer2 :-
    writeln('Wrong!').