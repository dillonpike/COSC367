leaves(tree([]), []).
leaves(tree([H|T]), [H|Leaves]) :- atom(H), leaves(tree(T), Leaves).
leaves(tree([H|T]), Leaves) :- leaves(H, L1), leaves(tree(T), L2), append(L1, L2, Leaves).


test_answer1 :- leaves(tree([the_only_leaf]), Leaves),
                writeln(Leaves).
               
test_answer2 :- leaves(tree([a, tree([b,c,d])]), L),
                writeln(L).