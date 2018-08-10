# Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.
#
# The data structure is a multi-dimensional Array(in Rust: Vec<Vec<u32>>) , ie:
#
# [
#   [7,8,4,  1,5,9,  3,2,6],
#   [5,3,9,  6,7,2,  8,4,1],
#   [6,1,2,  4,3,8,  7,5,9],
#
#   [9,2,8,  7,1,5,  4,6,3],
#   [3,5,7,  8,4,6,  1,9,2],
#   [4,6,1,  9,2,3,  5,8,7],
#
#   [8,7,6,  3,9,4,  2,1,5],
#   [2,4,3,  5,6,1,  9,7,8],
#   [1,9,5,  2,8,7,  6,3,4]
# ]
# Rules for validation
#
# Data structure dimension: NxN where N > 0 and √N == integer
# Rows may only contain integers: 1..N (N included)
# Columns may only contain integers: 1..N (N included)
# 'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)

import unittest


class Sudoku():
    # your code here
    def __init__(self, board):
        self.board = board

    def getHorizontal(self, board, index):
        return board[index]

    def getVertical(self, board, index):
        vertical = []
        for i in range(0, 9):
            vertical.append(board[i][index])
        return vertical

    def getBox(self, board, index):
        box = []
        lowerLimit = 3 * (index[0] - 1)
        upperLimit = 3 * index[0]
        for i in range(lowerLimit, upperLimit):
            box.extend(board[i][lowerLimit:upperLimit])
        return box

    def validateIndividualSudokuArray(self, array):
        valid_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if sorted(array) == valid_array:
            return True
        else:
            return False

    def validateHorizontalLines(self, sudokuArray):
        for i in range(0, 9):
            array = self.getHorizontal(sudokuArray, i)
            if self.validateIndividualSudokuArray(array):
                continue
            else:
                return False
        return True

    def validateVerticleLines(self, sudokuArray):
        for i in range(0, 9):
            array = self.getVertical(sudokuArray, i)
            if self.validateIndividualSudokuArray(array):
                continue
            else:
                return False
        return True

    def validateBoxes(self, sudokuArray):
        for i in range(1, 3):
            for j in range(1, 3):
                array = self.getBox(sudokuArray, [i, j])
                if self.validateIndividualSudokuArray(array):
                    continue
                else:
                    return False
        return True

    def is_valid(self):
        if not self.validateHorizontalLines(self.board):
            return False
        if not self.validateVerticleLines(self.board):
            return False
        if not self.validateBoxes(self.board):
            return False
        return True



abc = Sudoku([
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],

    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],

    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4]
])

print(abc.is_valid())

badSudoku1 = [
    [0, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

goodSudoku1 = [
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],

    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],

    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4]
]

def getHorizontal(sudoku, index):
    return sudoku[index]

def getVertical(sudoku, index):
    vertical = []
    for i in range(0, 9):
        vertical.append(sudoku[i][index])
    return vertical

def getDiagonal(sudoku, direction):
    diagonal = []
    if direction == "NW":
        for i in range(0, 9):
            diagonal.append(sudoku[i][i])
        return diagonal
    elif direction == "NE":
        for i in range(0,9):
            diagonal.append(sudoku[8-i][i])
        return diagonal

def getBox(sudoku, index):
    box = []
    lowerLimit = 3 * (index[0] - 1)
    upperLimit = 3 * index[0]
    for i in range(lowerLimit, upperLimit):
        box.extend(sudoku[i][lowerLimit:upperLimit])
    return box

def validateIndividualSudokuArray(sudoku):
    valid_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if sorted(sudoku) == valid_array:
        return True
    else:
        return False

def validateHorizontalLines(sudoku):
    for i in range(0, 9):
        array = getHorizontal(sudoku, i)
        if validateIndividualSudokuArray(array):
            continue
        else:
            return False
    return True

def validateVerticleLines(sudoku):
    for i in range(0, 9):
        array = getVertical(sudoku, i)
        if validateIndividualSudokuArray(array):
            continue
        else:
            return False
    return True

def validateDigonalLines(sudoku):
    for i in ["NE", "NW"]:
        array = getDiagonal(sudoku, i)
        if validateIndividualSudokuArray(array):
            continue
        else:
            return False
    return True

def validateBoxes(sudoku):
    for i in range(1, 3):
        for j in range(1, 3):
            array = getBox(sudoku, [i, j])
            if validateIndividualSudokuArray(array):
                continue
            else:
                return False
    return True

def validateSudoku(sudoku):
    if not validateHorizontalLines(sudoku):
        print("a")
        return False
    if not validateVerticleLines(sudoku):
        print("b")
        return False
    # if not validateDigonalLines(sudoku):
    #     print("c")
    #     return False
    if not validateBoxes(sudoku):
        print("d")
        return False
    return True


    # if index[0] == 1:
    #     for i in range(0, 3):
    #         if index[1] == 1:
    #             box.extend(sudoku[i][:3])
    #         elif index[1] == 2:
    #             box.extend(sudoku[i][3:6])
    #         elif index[1] == 2:
    #             box.extend(sudoku[i][6:9])
    #     return box
    # elif index[0] == 2:
    #     for i in range(3, 6):
    #         if index[1] == 1:
    #             box.extend(sudoku[i][:3])
    #         elif index[1] == 2:
    #             box.extend(sudoku[i][3:6])
    #         elif index[1] == 2:
    #             box.extend(sudoku[i][6:9])
    #     return box
    # elif index[0] == 2:
    #     for i in range(6, 9):
    #         if index[1] == 1:
    #             box.extend(sudoku[i][:3])
    #         elif index[1] == 2:
    #             box.extend(sudoku[i][3:6])
    #         elif index[1] == 2:
    #             box.extend(sudoku[i][6:9])
    #     return box



class TestCases(unittest.TestCase):

    def test_get_horizontal(self):
        self.assertEqual(getHorizontal(badSudoku1, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_get_vertical(self):
        self.assertEqual(getVertical(badSudoku1, 0), [0, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_get_diagonal_NE(self):
        self.assertEqual(getDiagonal(badSudoku1, "NE"), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_get_diagonal_NW(self):
        self.assertEqual(getDiagonal(badSudoku1, "NW"), [0, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_get_box(self):
        self.assertEqual(getBox(badSudoku1, [1, 1]), [0, 2, 3, 1, 2, 3, 1, 2, 3])

    def test_get_box_2(self):
        self.assertEqual(getBox(badSudoku1, [2, 2]), [4, 5, 6, 4, 5, 6, 4, 5, 6])

    def test_invalid_individual_sudoku_array(self):
        self.assertFalse(validateIndividualSudokuArray([0, 1, 1, 1, 1, 1, 1, 1, 1]))

    def test_valid_sudoku(self):
        self.assertTrue(validateSudoku(goodSudoku1))



if __name__ == '__main__':
    unittest.main()
