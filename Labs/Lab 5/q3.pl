tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([], []).
listtran([GH|GT], [EH|ET]) :- listtran(GT, ET), tran(GH, EH).


test_answer :-
    listtran([eins, neun, zwei], X),
    writeln(X).
