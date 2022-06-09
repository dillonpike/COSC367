max(L, R, L) :- L>=R.
max(L, R, R) :- R>=L.
max([H], H).
max([H1,H2|T], M) :- max(H1, H2, M2), max([M2|T], M).

test_answer1 :- 
    max([1, 2, 3, 4, 5], M),
    writeln(M).

test_answer2 :- 
    max([], M),
    writeln("Max of an empty list is undefined!").