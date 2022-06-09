split_odd_even([], [], []).
split_odd_even([X], [X], []).
split_odd_even([X,Y|InTail], [X|OutA], [Y|OutB]) :- split_odd_even(InTail, OutA, OutB).

merge(ListAIn, [], ListAIn).
merge([], ListBIn, ListBIn).
merge([HA|ListAIn], [HB|ListBIn], [HA|List]) :- HA=<HB, merge(ListAIn, [HB|ListBIn], List).
merge([HA|ListAIn], [HB|ListBIn], [HB|List]) :- HB<HA, merge([HA|ListAIn], ListBIn, List).

merge_sort([], []).
merge_sort([X], [X]).
merge_sort(ListIn, SortedList) :- 
        split_odd_even(ListIn, OutA, OutB),
        merge_sort(OutA, SortedA),
        merge_sort(OutB, SortedB),
        merge(SortedA, SortedB, SortedList).

test_answer :-
    merge_sort([4,3,1,2], L),
    writeln(L).