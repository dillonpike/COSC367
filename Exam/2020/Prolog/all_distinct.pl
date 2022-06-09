all_distinct([]).
all_distinct([H|T]) :- \+ member(H, T), all_distinct(T).

test_answer1 :- 
    all_distinct([1,2,3,4]),
    writeln('OK').

test_answer2 :- 
    all_distinct([a,b,c,b]),
    writeln("Wrong!").