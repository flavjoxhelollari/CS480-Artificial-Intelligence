### eightPuzzle.py
### Solution to the second part of the first Python Programming Assignment
### Flavjo Xhelollari 001381100

from informedSearch import *

class EightPuzzleState(InformedProblemState):
    """
    Goal state is a 3 by 3 matrix which should look like :
    1 2 3
    8 0 4
    7 6 5
    Note : 0 represents the empty spot.

        Node Expansions
    Problem   BFS   A*(tiles)  A*(dist)
    a          4        3           3
    b         77        8           7
    c        179       18          10
    d        666       48          20
    e        809       44          20
    f       1843      110         123
    g       5396      375          61
    """

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __str__(self):
        """
        Required method from Searh Class
        Returns a string representation of the state.
        """
        return self.puzzle

    def illegal(self):
        """
        Required method from Search Class
        Tests if the state is illegal (it returns -1), and returns 1
        """
        if self.puzzle == -1 : return 1
        return 0

    def equals(self, state) :
        """
        Required method from Search Class.
        Finds if state instance and given state are equal.
        """

        return self.puzzle == state.puzzle

    def moveRight(self):
        """
        Moves 0 to the right and if it is in the proper column,
        returns -1
        """
        zero_index = self.puzzle.index('0')
        if zero_index in (2,5,8):
            return EightPuzzleState(-1)
        else :
            newPuzzle = ""
            newPuzzle = self.puzzle[0: zero_index] + self.puzzle[zero_index + 1] + '0' + self.puzzle[zero_index + 2:]
            return EightPuzzleState(newPuzzle)
    def moveLeft(self):
        """
        Moves 0 to the left and if it is in the proper column,
        returns -1
        """
        zero_index = self.puzzle.index('0')
        if zero_index in (0,3,6):
            return EightPuzzleState(-1)
        else :
            newPuzzle = ""
            newPuzzle = self.puzzle[0: zero_index - 1] + '0' + self.puzzle[zero_index - 1] + self.puzzle[zero_index + 1:]
            return EightPuzzleState(newPuzzle)

    def moveUp(self):
        """
        Moves 0 up and if it is in the top row,
        returns -1
        """
        zero_index = self.puzzle.index('0')
        if zero_index in (0,1,2):
            return EightPuzzleState(-1)
        else :
            newPuzzle = ""
            newPuzzle = self.puzzle[0: zero_index - 3] + '0' + self.puzzle[zero_index - 2 : zero_index] + self.puzzle[zero_index - 3] + self.puzzle[zero_index + 1 :]

            return EightPuzzleState(newPuzzle)

    def moveDown(self):
        """
        Moves 0 down one value and if it is in the bottom row,
        returns -1
        """
        zero_index = self.puzzle.index('0')
        if zero_index in (6,7,8):
            return EightPuzzleState(-1)
        else :
            newPuzzle = ""
            newPuzzle = self.puzzle[0: zero_index] + self.puzzle[zero_index + 3] + self.puzzle[zero_index + 1 : zero_index + 3] + '0' + self.puzzle[zero_index + 4 :]
            return EightPuzzleState(newPuzzle)


    def operatorNames(self):
        """
        Required method from Search Class.
        Returns a list of operator names in
        the same order as applyOperators method
        """
        return["moveLeft", "moveRight", "moveUp", "moveDown"]

    def applyOperators(self):
        """
        Required method from Searh class.
        Returns a list of possible successors
        to the current state, some maybe illegal.
        """
        return [self.moveLeft(), self.moveRight(), self.moveUp(), self.moveDown()]

    def heuristic(self, goal):
        """
        Required method from informedSearch class.
        Executes Manhattan Distance, Tiles Out of Place
        or Breadth First Search heuristic (uncommented).
        """
        # sum = 0
        # sum = EightPuzzleState.outOfPlace(self, goal)
        sum = EightPuzzleState.manhattan(self, goal)
        return sum

    def manhattan(self, goal):
        """
        Calculates Manhattan Distance and returns the sum.
        """
        sum = 0
        for i in goal.puzzle:
            sum += abs(self.puzzle.index(i) - goal.puzzle.index(i))
        return sum

    def outOfPlace(self, goal):
        """
        Return the number of values that are misplaced in the puzzle.
        """
        sum = 0
        for i in range(9):
            if self.puzzle[i] != goal.puzzle[i]:
                sum += 1
        return sum



def main():

    goal = "123804765"
    a = "130824765"
    b = "134862075"
    c = "013425876"
    d = "712803654"
    e = "812704653"
    f = "263405187"
    g = "734615802"
    h = "745603812"


    InformedSearch(EightPuzzleState(a), EightPuzzleState(goal))
    InformedSearch(EightPuzzleState(b), EightPuzzleState(goal))
    InformedSearch(EightPuzzleState(c), EightPuzzleState(goal))
    InformedSearch(EightPuzzleState(d), EightPuzzleState(goal))
    InformedSearch(EightPuzzleState(e), EightPuzzleState(goal))
    InformedSearch(EightPuzzleState(f), EightPuzzleState(goal))
    InformedSearch(EightPuzzleState(g), EightPuzzleState(goal))
    InformedSearch(EightPuzzleState(h), EightPuzzleState(goal))

main()
