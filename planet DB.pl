planet(mercury).
planet(venus).
planet(earth).
planet(mars).
planet(jupiter).
planet(saturn).
planet(uranus).
planet(neptune).

get_planet :-
    findall(Planet, planet(Planet), Planets),
    write_list(Planets).
write_list([]).
write_list([X|Xs]) :-
    write(X), write(' '),
    write_list(Xs).

