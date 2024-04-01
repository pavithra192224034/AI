% Define facts about fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(watermelon, green).

% Define a predicate to query for fruit-color pairs
fruit_color_query(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Define a predicate to query for all fruits of a given color
fruits_of_color(Color, Fruits) :-
    findall(Fruit, fruit_color(Fruit, Color), Fruits).

% Define a predicate to query for all colors of a given fruit
colors_of_fruit(Fruit, Colors) :-
    findall(Color, fruit_color(Fruit, Color), Colors).
