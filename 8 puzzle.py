import heapq

# Goal state of the 8-puzzle
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]


# Function to find the coordinates of a number in the puzzle
def find_coord(puzzle, num):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == num:
                return i, j


# Function to calculate the Manhattan distance heuristic
def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                x, y = find_coord(goal_state, puzzle[i][j])
                distance += abs(x - i) + abs(y - j)
    return distance


# Function to generate possible moves
def generate_moves(puzzle):
    moves = []
    x, y = find_coord(puzzle, 0)

    if x > 0:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[x][y], new_puzzle[x - 1][y] = new_puzzle[x - 1][y], new_puzzle[x][y]
        moves.append((new_puzzle, manhattan_distance(new_puzzle)))

    if x < 2:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[x][y], new_puzzle[x + 1][y] = new_puzzle[x + 1][y], new_puzzle[x][y]
        moves.append((new_puzzle, manhattan_distance(new_puzzle)))

    if y > 0:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[x][y], new_puzzle[x][y - 1] = new_puzzle[x][y - 1], new_puzzle[x][y]
        moves.append((new_puzzle, manhattan_distance(new_puzzle)))

    if y < 2:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[x][y], new_puzzle[x][y + 1] = new_puzzle[x][y + 1], new_puzzle[x][y]
        moves.append((new_puzzle, manhattan_distance(new_puzzle)))

    return moves


# A* algorithm to solve the puzzle
def a_star(puzzle):
    initial_state = (puzzle, manhattan_distance(puzzle))
    frontier = [initial_state]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        current_state = heapq.heappop(frontier)
        current_puzzle, current_cost = current_state

        if current_puzzle == goal_state:
            return current_puzzle

        explored.add(str(current_puzzle))

        for move in generate_moves(current_puzzle):
            if str(move[0]) not in explored:
                heapq.heappush(frontier, move)

    return "No solution"


# Example usage
initial_puzzle = [[1, 2, 3],
                  [4, 5, 6],
                  [0, 7, 8]]

solution = a_star(initial_puzzle)
if solution == "No solution":
    print("No solution exists for the given puzzle.")
else:
    print("Solution found:")
    for row in solution:
        print(row)
