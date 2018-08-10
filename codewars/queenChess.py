# Task:
# Write a function availableMoves(position) which returns possibly moves of chess queen. Returned value should be an array
# with possible moves sorted alphabetically, exluded starting position.
#
# For example when input position is A1 return value should be:
#
# ["A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "C1", "C3", "D1", "D4", "E1", "E5", "F1", "F6", "G1", "G7", "H1", "H8"]
#
# Input:
# input position can be any type (array, number, string and so on). If input position is not a string then return empty
# array.
# valid input position is one letter from A to H with number from 1 to 8, for example A1, C8, B3. If input is invalid
# (for example A10 or H0) then return empty array.

import unittest

def isInputValid(position):
    if not isinstance(position, str):
        return False
    x = position[0]
    y = position[1:]
    validAlpha = ["A", "B", "C", "D", "E", "F", "H", "G"]
    validNumber = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if x in validAlpha and y in validNumber:
        return True
    else:
        return False

def availableMoves(position):
    moves = []
    if not isInputValid(position):
        return moves
    x = position[0]
    y = position[1:]
    validAlpha = ["A", "B", "C", "D", "E", "F", "G", "H"]
    validNumber = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for i in validNumber:
        moves.append(x + i)
    for i in validAlpha:
        moves.append(i + y)
    xIndex = validAlpha.index(x)
    yIndex = validNumber.index(y)
    for i in range(1, len(validAlpha)):
        if (xIndex + i) < len(validAlpha) and (yIndex + i) < len(validNumber):
            testPosition = validAlpha[xIndex + i] + validNumber[yIndex + i]
            if isInputValid(testPosition):
                moves.append(testPosition)
        if (xIndex - i) >= 0 and (yIndex - i) >= 0:
            testPosition = validAlpha[xIndex - i] + validNumber[yIndex - i]
            if isInputValid(testPosition):
                moves.append(testPosition)
        if (xIndex - i) >= 0 and (yIndex + i) < len(validNumber):
            testPosition = validAlpha[xIndex - i] + validNumber[yIndex + i]
            if isInputValid(testPosition):
                moves.append(testPosition)
        if (xIndex + i) < len(validAlpha) and (yIndex - i) >= 0:
            testPosition = validAlpha[xIndex + i] + validNumber[yIndex - i]
            if isInputValid(testPosition):
                moves.append(testPosition)
    moves = [x for x in moves if x != position]
    moves = sorted(moves)
    return moves

{"NE": [1, 1], NW}

def diagonal(dict[NE])




class TestCases(unittest.TestCase):

    def test_out_of_bounds(self):
        self.assertFalse(isInputValid("A10"))

    def test_valid(self):
        self.assertTrue(isInputValid("A1"))

    def test_input_not_string(self):
        self.assertFalse(availableMoves(9), [])

    def test_valid(self):
        self.assertEqual(availableMoves("A1"), ["A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "C1", "C3", "D1", "D4", "E1", "E5", "F1", "F6", "G1", "G7", "H1", "H8"])


