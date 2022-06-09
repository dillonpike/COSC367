member(X, [X|T]).
member(X, [H|T]) :- member(X, T).

unique([], []).
unique([H|T], [H|Set]) :- not(member(H, T)), unique(T, Set).
unique([H|T], Set) :- member(H, T), unique(T, Set).


test_answer1 :- 
    unique([1,2,1,4,3,3], Set),
    sort(Set,Sorted),
    writeln(Sorted).

test_answer2 :- 
    unique([], Set),
    sort(Set,Sorted),
    writeln(Sorted).