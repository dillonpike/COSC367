match(L, R) :- (L=c, R=g); (L=a, R=t); (L=g, R=c); (L=t, R=a).
dna([], []).
dna([LH|LT], [RH|RT]) :- match(LH, RH), dna(LT, RT).

test_answer1 :- dna([a, t, c, g], X),
               writeln(X).

test_answer2 :- dna(X, [t, a, g, c]),
               writeln(X).