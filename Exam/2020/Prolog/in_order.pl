inorder(leaf(X), [X]).
inorder(tree(Root, L, R), T) :- inorder(L, LT), inorder(R, RT), append(LT, [Root|RT], T).

test_answer1 :- inorder(tree(1, leaf(2), leaf(3)), T), writeln(T).
test_answer2 :- inorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).