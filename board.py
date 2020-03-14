def set_list(n):
    list = []
    for i in range(n):
        list.append([0] * n)
    return list


class empty:
    name = '-'
    colour = ''
    available = []
    position = None


class board:
    """The Board class."""

    def __init__(self, n):
        self.n = n
        self.status = set_list(n)
        self.create(n)

    check = [False, None]

    # check[0] indicates if one side checked the other
    # check[1] indicates which side checked

    # n is the grade of the board. In a standard chess game, the grade is 8.
    # The 'status' attribute contains an array representing the current state of the game.

    def create(self, n):
        for i in range(n):
            for j in range(n):
                self.set_piece(empty(), [chr(65 + i), j + 1])
        return True

    # 'create' fills the board with empty tiles.

    def piece(self, c):
        y, x = ord(c[0]), int(c[1])
        return self.status[self.n - (y - 64)][x - 1]

    # The 'piece' method returns the object corresponding to the coordinates given. Coordinates are given in list format.

    def set_piece(self, piece, c):
        y, x = ord(c[0]), int(c[1])
        self.status[self.n - (y - 64)][x - 1] = piece
        piece.board = self
        piece.position = c
        return True

    # The 'set_piece' method sets a piece on the board on the given coordinates.
    # Also the coordinates are set in the 'position' attribute of the piece, so that its 'move' function can be called.

    def move(self, inc, outc):
        if outc in self.piece(inc).available or outc == self.piece(inc).available:
            self.set_piece(self.piece(inc), outc)
            self.set_piece(empty(), inc)
            self.update()
            return True
        else:
            return False

    # 'move' sets a piece to outc while leaving an empty piece at inc, but only if the piece can be moved to outc

    def check_border(self, c):
        if ord(c[0]) > 64 + self.n or ord(c[0]) < 65 or c[1] < 1 or c[1] > self.n:
            return True
        else:
            return False

    # 'check_border' looks if the coordinates c are on the board. It gets used in the 'check_available' method of every piece

    def check_king(self, available):
        if available:
            for i in available:
                if self.piece(i).name == 'King':
                    return True
        return False

    def update(self, colour):
        check = [False, None]
        for i in range(self.n):
            for j in range(self.n):
                if self.status[i][j].colour == colour and self.status[i][j].name != '-':
                    self.status[i][j].check_available()
                    if self.check_king(self.status[i][j].available):
                        check = [True, self.status[i][j].colour]
                    else:
                        pass
        self.check = check
        return True

    # 'update' actualizes the available attribute of every piece

    def print_status(self, status):
        print('\n')
        for h in range(self.n):
            a = [chr(64 + self.n - h)]
            for i in range(self.n):
                if status[h][i].name != '-':
                    a.append(''.join(list(status[h][i].name)[:2]) + '(' + status[h][i].colour + ')')
                else:
                    a.append('  -  ')
            print(' '.join(a))
        a = [' ']
        for j in range(1, self.n + 1):
            a.append('  ' + str(j) + '  ')
        print(' '.join(a), '\n')
