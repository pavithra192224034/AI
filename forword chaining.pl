:- dynamic has_symptom/1. % Declare dynamic predicate
% Define facts and rules
hypothesis(has_flu) :- symptom(fever), symptom(cough), symptom(fatigue).
hypothesis(has_cold) :- symptom(runny_nose), symptom(sneezing).

% Define symptoms directly as facts
symptom(fever).
symptom(cough).
symptom(fatigue).
symptom(runny_nose).
symptom(sneezing).

% Define backward chaining algorithm
forward_chaining(Disease) :-
    hypothesis(Disease),
    write('Patient may have: '), write(Disease), nl,
    !. % Cut to stop further backtracking

forward_chaining(Disease) :-
    symptom(Disease),
    write('Patient may have: '), write(Disease), nl,
    fail.

forward_chaining(Disease) :-
    write('Could not determine the disease based on the given symptoms.'), nl.

% Example queries
% To check if the patient has flu:
% ?- backward_chaining(has_flu).
%
% To check if the patient has cold:
% ?- backward_chaining(has_cold).
%
% To infer potential diseases based on symptoms:
% ?- backward_chaining(Disease).
