word(astante, a,s,t,a,n,t,e).
word(astoria, a,s,t,o,r,i,a).
word(baratto, b,a,r,a,t,t,o).
word(cobalto, c,o,b,a,l,t,o).
word(pistola, p,i,s,t,o,l,a).
word(statale, s,t,a,t,a,l,e).

solution(V1,V2,V3,H1,H2,H3) :-
        word(V1, V11,V1H1,V12,V1H2,V13,V1H3,V14),
        word(V2, V21,V2H1,V22,V2H2,V23,V2H3,V24),
        word(V3, V31,V3H1,V32,V3H2,V33,V3H3,V34),
        word(H1, H11,V1H1,H12,V2H1,H13,V3H1,H14),
        word(H2, H21,V1H2,H22,V2H2,H23,V3H2,H24),
        word(H3, H31,V1H3,H32,V2H3,H33,V3H3,H34).

test_answer :-
    findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
    sort(L,S),
    foreach(member(X,S), (write(X), nl)).

test_answer :- write('Wrong answer!'),
    halt.
