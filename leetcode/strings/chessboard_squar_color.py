'''
Leetcode #1812: Determine Color of a Chessboard Square

You are given coordinates, a string that represents the coordinates 
of a square of the chessboard. Below is a chessboard for your reference.
Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. 
The coordinate will always have the letter first, and the number second.
'''


def squareIsWhite(coordinates: str) -> bool:
        x_axis = ord('a') - ord(coordinates[0]) + 1
        y_axis = int(coordinates[1])

        return not ((x_axis + y_axis) % 2 == 0)
        