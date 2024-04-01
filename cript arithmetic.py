# Recursive function to solve the puzzle
def solve_cryptarithmetic(puzzle, assignment, index, carry):
    if index == len(puzzle):
        return True

    current_char = puzzle[index]

    # If the character is already assigned, move to the next one
    if current_char in assignment:
        return solve_cryptarithmetic(puzzle, assignment, index + 1, carry)

    # Try assigning each digit from 0 to 9
    for digit in range(10):
        if digit not in assignment.values():
            assignment[current_char] = digit
            if solve_cryptarithmetic(puzzle, assignment, index + 1, carry):
                return True
            del assignment[current_char]

    return False


# Function to check if a given assignment is valid
def is_valid_assignment(assignment, puzzle):
    # Extract values corresponding to each word in the puzzle and sum them up
    values = [sum(assignment[char] * (10 ** (len(word) - i - 1)) for i, char in enumerate(word)) for word in puzzle if word.isalpha()]
    return sum(values[:-1]) == values[-1]


# Main function to solve the puzzle
def solve(puzzle):
    unique_chars = set(char for word in puzzle for char in word if char.isalpha())
    if len(unique_chars) > 10:
        print("Invalid puzzle. More than 10 unique letters.")
        return

    assignment = {}
    puzzle = ''.join(puzzle)

    if solve_cryptarithmetic(puzzle, assignment, 0, 0) and is_valid_assignment(assignment, puzzle):
        for char in puzzle:
            if char.isalpha():
                print(f"{char}: {assignment[char]}")
    else:
        print("No solution exists.")


# Example usage
puzzle = ["SEND", "+", "MORE", "=", "MONEY"]
solve(puzzle)
