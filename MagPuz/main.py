# In this code i will go out from the board in assignment 1, problem 3.

# First we need the size of the board
# M = rows / height of the board
# N = coulms / width of the board
M = 5
N = 6

# Then we need to set the constraints on the sides of the board.
# Top and right side are +, and bottom and left side are -.
# -1 in the constraints means any number can be placed here.
top = [1, -1, -1, 2, 1, -1]
left = [2, 3, -1, -1, -1]
bottom = [2, -1, -1, 2, -1, 3]
right = [-1, -1, -1, 1, -1]

# Then we need the rules of the board.
# Where can the pieces be placed.

rules = [['L', 'R', 'L', 'R', 'T', 'T'],
         ['L', 'R', 'L', 'R', 'B', 'B'],
         ['T', 'T', 'T', 'T', 'L', 'R'],
         ['B', 'B', 'B', 'B', 'T', 'T'],
         ['L', 'R', 'L', 'R', 'B', 'B']]

# To count the number of visited nodes, we store them here.
visitedNodes = []

# Count promising nodes
promisingNodes = []

# Now we can start to make the program to solve the problem.
# This is the main function to solve the puzzle.
def magnets(rules, i, j):
    visitedNodes.append(rules)
    print("Rules:")
    print(rules)

    # First we check if the last cell of the board is reached
    if i >= M - 1 and j >= N - 1:
        print("Last cell of board?!")


    # If we have reached the bottom of a rule constraint.
    # We skip it to the next cell because we have already placed something there from the last row.
    #if rules[i][j] == 'B': # or rules[i][j] == 'R':
     #   j = j + 1

    # Then check if the last cell of the row is reached
    if j >= N:
        j = 0
        i = i + 1

    # First check if te piece needs to be placed horizontally
    if rules[i][j] == 'L':  # or rules[i][j] == 'R':

        # because the rules in this position is 'L', we know we can put a piece horizontally
        # We have three options, we can put it '+-', '-+' or 'XX'
        # alternative 1
        if canPutHorizontally(rules, i, j, '+-'):
            rules[i][j] = '+'
            rules[i][j + 1] = '-'


            # Here we run magnets recursively
            magnets(rules, i, j + 2)

            # If we go back from a recursive magnet, we need to place back L and R in the rules
            rules[i][j] = 'L'
            rules[i][j + 1] = 'R'

        # alternative 2
        if canPutHorizontally(rules, i, j, '-+'):
            rules[i][j] = '-'
            rules[i][j + 1] = '+'

            magnets(rules, i, j + 2)

            # If we go back from a recursive magnet, we need to place back L and R in the rules
            rules[i][j] = 'L'
            rules[i][j + 1] = 'R'

        # alternative 3
        if canPutHorizontally(rules, i, j, 'xx'):
            rules[i][j] = 'x'
            rules[i][j + 1] = 'x'

            magnets(rules, i, j + 2)

            # If we go back from a recursive magnet, we need to place back L and R in the rules
            rules[i][j] = 'L'
            rules[i][j + 1] = 'R'

    # Then check if the piece needs to be placed vertically
    elif rules[i][j] == 'T':  # or rules[i][j] == 'B':
        # because the rules in this position is 'T', we know we can put a piece vertically
        # We have three options, we can put it '+-', '-+' or 'XX'. First symbol at the top
        # alternative 1
        if canPutVertically(rules, i, j, '+-'):
            rules[i][j] = '+'
            rules[i + 1][j] = '-'

            # Here we run magnets recursively
            magnets(rules, i, j + 1)

            # If we go back from a recursive magnet, we need to place back L and R in the rules
            rules[i][j] = 'T'
            rules[i + 1][j] = 'B'

        # alternative 2
        if canPutVertically(rules, i, j, '-+'):
            rules[i][j] = '-'
            rules[i + 1][j] = '+'

            magnets(rules, i, j + 1)

            # If we go back from a recursive magnet, we need to place back L and R in the rules
            rules[i][j] = 'T'
            rules[i + 1][j] = 'B'

        # alternative 3
        if canPutVertically(rules, i, j, 'xx'):
            rules[i][j] = 'x'
            rules[i + 1][j] = 'x'

            magnets(rules, i, j + 1)

            # If we go back from a recursive magnet, we need to place back L and R in the rules
            rules[i][j] = 'T'
            rules[i + 1][j] = 'B'
    #else:
        #print("Error") # Remove?

# Function to check if a piece can be placed horizontally
def canPutHorizontally(rules, i, j, pattern):
    # Checking which way the piece will be placed '+-'
    if pattern[0] == '+':
        # Checking the neighbouring squares.
        if j-1 >= 0 and rules[i][j - 1] == '+':
            return False
        if i-1 >= 0 and rules[i - 1][j] == '+':
            return False
        if i+1 < M and rules[i + 1][j] == '+':
            return False
        if i+1 < M and j+1 < N and rules[i + 1][j + 1] == '-':
            return False
        if j+2 < N and rules[i][j + 2] == '-':
            return False
        if i-1 >= 0 and j+1 < N and rules[i - 1][j + 1] == '-':
            return False

        # Then check if the top and side rules are ok
        if not checkSideConstraints(rules, i, j):
            return False

    # Checking the neighbouring squares if the piece is placed the other way
    elif pattern[0] == '-':
        # Checking the neighbouring squares
        if j-1 >= 0 and rules[i][j - 1] == '-':
            return False
        if i-1 >= 0 and rules[i - 1][j] == '-':
            return False
        if i+1 < M and rules[i + 1][j] == '-':
            return False
        if i+1 < M and j+1 < N and rules[i + 1][j + 1] == '+':
            return False
        if j+2 < N and rules[i][j + 2] == '+':
            return False
        if i-1 >= 0 and j+1 < N and rules[i - 1][j + 1] == '+':
            return False

        # Then checking if the top, bot and sides are ok.
        if not checkSideConstraints(rules, i, j):
            return False

    # The piece can be placed, and the function returns True
    return True


# Function to check if a piece can be placed vertically
def canPutVertically(rules, i, j, pattern):
    # Checking which way the piece will be placed
    if pattern[0] == '+':
        # Check neighbouring squares
        if j-1 >= 0 and rules[i][j - 1] == '+':
            return False
        if i-1 >= 0 and rules[i - 1][j] == '+':
            return False
        if j+1 < N and rules[i][j + 1] == '+':
            return False
        if i+1 < M and j-1 >= 0 and rules[i + 1][j - 1] == '-':
            return False
        if i + 2 < M and rules[i + 2][j] == '-':
            return False
        if i+1 < M and j+1 < N and rules[i + 1][j + 1] == '-':
            return False

        # Then check if the top and side rules are ok
        if not checkSideConstraints(rules, i, j):
            return False

    elif pattern[0] == '-':
        # Checking neighbouring squares
        if j-1 >= 0 and rules[i][j - 1] == '-':
            return False
        if i-1 >= 0 and rules[i -1][j] == '-':
            return False
        if j+1 < N and rules[i][j + 1] == '-':
            return False
        if i+1 < M and j-1 >= 0 and rules[i + 1][j - 1] == '+':
            return False
        if i+2 < M and rules[i + 2][j] == '+':
            return False
        if i+1 < M and j+1 < N and rules[i + 1][j + 1] == '+':
            return False

        # Then check if the top and side rules are ok
        if not checkSideConstraints(rules, i, j):
            return False

    # The piece can be placed, and the function returns True
    return True


# Function to count the number of '+' or '-' in the given column of the board
def numberInColumn(rules, j, sym):
    number = 0
    for i in range(M):
        if rules[i][j] == sym:
            number = number + 1
    return number


# Function to count the number of '+' or '-' in the given row of the board
def numberInRow(rules, i, sym):
    number = 0
    for j in range(N):
        if rules[i][j] == sym:
            number = number + 1
    return number


# Function to check the side constraints rules.
def checkSideConstraints(rules, i, j, ):
    # Number of '+' and '-' in the column:
    columnCountPlus = numberInColumn(rules, j, '+')
    columnCountMinus = numberInColumn(rules, j, '-')

    # Number of '+' and '-' in the row
    rowCountPlus = numberInRow(rules, i, '+')
    rowCountMinus = numberInRow(rules, i, '-')

    # Then use the numbers to check with the constraints
    if top[j] != -1 and columnCountPlus >= top[j]:
        return False
    if bottom[j] != -1 and columnCountMinus >= bottom[j]:
        return False
    if left[i] != -1 and rowCountPlus >= left[i]:
        return False
    if right[i] != -1 and rowCountMinus >= right[i]:
        return False

    # If side constraints are ok return True
    return True


# Start the program with the rules and a starting point on the board top left (0,0).
if magnets(rules, 0, 0):
    print(rules)
    print(len(visitedNodes))
    print(len(promisingNodes))
