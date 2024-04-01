% Facts about birds and whether they can fly
can_fly(pigeon).
can_fly(sparrow).
can_fly(eagle).

% Queries
% Query to check if a bird can fly
can_fly(X) :-
    can_fly(X),
    write(X), write(' can fly.').

% Query to check if a bird cannot fly
cannot_fly(X) :-
    \+ can_fly(X),
    write(X), write(' cannot fly.').

% Example queries
% Query to check if pigeon can fly
% Output: pigeon can fly.
 can_fly(pigeon).

% Query to check if penguin can fly
% Output: penguin cannot fly.
 cannot_fly(penguin).
