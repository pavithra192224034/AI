:- use_module(library(lists)).

% bfs(Start, Goal, Solution)
% Predicate to find a solution path from Start to Goal using BFS.
bfs(Start, Goal, Solution) :-
    bfs([[Start]], Goal, Solution).

% bfs(Queue, Goal, Solution)
% Base case: The first element of the queue is the goal state. Return the path.
bfs([[Goal|Path]|_], Goal, [Goal|Path]).

% bfs(Queue, Goal, Solution)
% Recursive case: Expand the first node in the queue and add its successors to the queue.
bfs([Path|Paths], Goal, Solution) :-
    extend(Path, NewPaths),
    append(Paths, NewPaths, Queue),
    bfs(Queue, Goal, Solution).

% extend(Path, NewPaths)
% Generate all possible extensions of a path by adding one more node to it.
extend([Node|Path], NewPaths) :-
    findall([NewNode, Node|Path],
            (move(Node, NewNode), not(member(NewNode, [Node|Path]))),
            NewPaths).

% Define the move predicate according to your problem domain.
% For example:
move(a, b).
move(b, c).
move(c, d).
move(b, e).
move(d, f).
