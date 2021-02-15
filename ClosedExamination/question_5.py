import copy


class Blotris:
    def __init__(self, rows, cols):
        if rows < 5 or cols < 5:
            raise ValueError()
        self._cols = cols
        self._board = [[0 for y in range(cols)] for x in range(rows)]

    def add(self, shape: list, row: int, col: int):
        # Copy board to prevent live-editing
        new_board = copy.deepcopy(self._board)
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                x_fill, y_fill = x+col, y+row
                # Return False if co-ords are outside board bounds
                if y_fill >= len(self._board) or y_fill < 0:
                    return False
                if x_fill >= len(self._board[0]) or x_fill < 0:
                    return False
                if shape[y][x] == 1:
                    # Verify cell is empty then fill, otherwise return False
                    if self._board[y_fill][x_fill] == 1:
                        return False
                    else:
                        new_board[y_fill][x_fill] = 1
        # Update board if shape placement was successful
        self._board = new_board
        return True

    def update(self):
        for y in range(len(self._board)):
            if 0 not in self._board[y]:
                # copy to row from row above
                for i in range(y, 0, -1):
                    self._board[i] = self._board[i-1]
                # new row is set to 0
                self._board[0] = [0 for c in range(self._cols)]
