merge(ListAIn, [], ListAIn).
merge([], ListBIn, ListBIn).
merge([HA|ListAIn], [HB|ListBIn], [HA|List]) :- HA=<HB, merge(ListAIn, [HB|ListBIn], List).
merge([HA|ListAIn], [HB|ListBIn], [HB|List]) :- HB<HA, merge([HA|ListAIn], ListBIn, List).


test_answer1 :-
    merge([3, 6, 7], [1, 2, 3, 5, 8], L),
    writeln(L).

test_answer2 :-
    merge([3, 6, 7], [], L),
    writeln(L).