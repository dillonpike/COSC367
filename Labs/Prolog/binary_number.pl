binary_digit(D) :- D=0; D=1.
binary_digits([H|T]) :- binary_digit(H), (T=[]; binary_digits(T)).
binary_number([0,b|T]) :- binary_digits(T).

test_answer1 :- binary_number([0, b, 1, 0, 1]), 
               writeln('OK').

test_answer2 :- binary_number([0, b, 0, 1, 2]), 
               writeln('Wrong!'), halt.
test_answer2 :- writeln('OK').