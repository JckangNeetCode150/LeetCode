from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Initializes defaultdict(set) for rows, columns, and square dictionaries
        rowDictionary = defaultdict(set)
        columnDictionary = defaultdict(set)
        squareDictionary = defaultdict(set)

        # Iterate through each cell in the Sudoku board (row outside, column inside)
        for row in range(len(board)):
            for column in range(len(board)):

                # Ignore row cell containing "."
                if board[row][column] != ".":

                    # Check if rowDictionary["R" + str(row + 1)] contains current row cell
                    if board[row][column] in rowDictionary["R" + str(row + 1)]:
                        return False

                    # Add the current value to "rowdictionary"
                    rowDictionary["R" + str(row + 1)].add(board[row][column])

                    # Check if squareDictionary["S[" + str(row//3) + "]" + "[" + str(column//3) + "]"] contains current square value
                    if board[row][column] in squareDictionary["S[" + str(row//3) + "]" + "[" + str(column//3) + "]"]:
                        return False

                    # Add the current value to "squaredictionary"
                    squareDictionary["S[" + str(row//3) + "]" +
                                     "[" + str(column//3) + "]"].add(board[row][column])

                # Ignore column cell containing "."
                if board[column][row] != ".":

                    # Check if columnDictionary["C" + str(row + 1)] contains current column cell
                    if board[column][row] in columnDictionary["C" + str(row + 1)]:
                        return False

                    # Add the current value to "columndictionary"
                    columnDictionary["C" +
                                     str(row + 1)].add(board[column][row])

        return True
