class piece:
    """Standard chess piece"""

    def __init__(self, colour):
        self.colour = colour
        self.position = None
        self.board = None
        self.available = []


class pawn(piece):
    """Pawn piece"""
    name = 'Pawn'

    def __init__(self, colour):
        super().__init__(colour)

    def check_available(self):
        self.available = []
        if self.colour == 'W':
            direction = 1
        elif self.colour == 'B':
            direction = -1
        for i in range(-1, 2):
            if not self.board.check_border((chr(ord(self.position[0]) + i), self.position[1] + direction)):
                c = (chr(ord(self.position[0]) + i), self.position[1] + direction)
                if self.board.piece(c).name == '-' and i == 0:
                    self.available.append(c)
                    if self.colour == 'W' and self.position[1] == 2 and self.board.piece(
                            (self.position[0], 4)).name == '-':
                        self.available.append((self.position[0], 4))
                    elif self.colour == 'B' and self.position[1] == self.board.n - 1 and self.board.piece(
                            (self.position[0], self.position[1] - 2)).name == '-':
                        self.available.append((self.position[0], self.position[1] - 2))
                elif self.board.piece(c).name != '-' and self.board.piece(c).colour != self.colour:
                    self.available.append(c)
    # 'check_available' creates a list of coordinates the pawn is able to move towards.


class knight(piece):
    """Knight piece"""
    name = 'Knight'

    def __init__(self, colour):
        super().__init__(colour)

    def check_available(self):
        self.available = []
        for i in range(-2, 5, 4):
            for j in range(-1, 2, 2):
                if not self.board.check_border((chr(ord(self.position[0]) + i), self.position[1] + j)):
                    c = (chr(ord(self.position[0]) + i), self.position[1] + j)
                    if self.board.piece(c).name == '-' or self.board.piece(c).colour != self.colour:
                        self.available.append(c)
        for k in range(-2, 5, 4):
            for l in range(-1, 2, 2):
                if not self.board.check_border((chr(ord(self.position[0]) + l), self.position[1] + k)):
                    c = (chr(ord(self.position[0]) + l), self.position[1] + k)
                    if self.board.piece(c).name == '-' or self.board.piece(c).colour != self.colour:
                        self.available.append(c)


class bishop(piece):
    """Bishop piece"""
    name = 'Bishop'

    def __init__(self, colour):
        super().__init__(colour)

    def check_available(self):
        self.available = []
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                if not self.board.check_border((chr(ord(self.position[0]) + i), self.position[1] + j)):
                    c = (chr(ord(self.position[0]) + i), self.position[1] + j)
                    while self.board.piece(c).name == '-':
                        self.available.append(c)
                        if not self.board.check_border((chr(ord(c[0]) + i), c[1] + j)):
                            c = (chr(ord(c[0]) + i), c[1] + j)
                        else:
                            break
                    if self.board.piece(c).colour != self.colour and self.board.piece(c).colour != '':
                        self.available.append(c)


class rook(piece):
    """Rook Piece"""
    name = 'Rook'

    def __init__(self, colour):
        super().__init__(colour)

    def check_available(self):
        self.available = []
        for i in range(-1, 2, 2):
            if not self.board.check_border((chr(ord(self.position[0]) + i), self.position[1])):
                c = (chr(ord(self.position[0]) + i), self.position[1])
                while self.board.piece(c).name == '-':
                    self.available.append(c)
                    if not self.board.check_border([chr(ord(c[0]) + i), c[1]]):
                        c = (chr(ord(c[0]) + i), c[1])
                    else:
                        break
                if self.board.piece(c).colour != self.colour and self.board.piece(c).colour != '':
                    self.available.append(c)
        for j in range(-1, 2, 2):
            if not self.board.check_border((self.position[0], self.position[1] + j)):
                c = (self.position[0], self.position[1] + j)
                while self.board.piece(c).name == '-':
                    self.available.append(c)
                    if not self.board.check_border([c[0], c[1] + j]):
                        c = (c[0], c[1] + j)
                    else:
                        break
                if self.board.piece(c).colour != self.colour and self.board.piece(c).colour != '':
                    self.available.append(c)


class queen(piece):
    """Queen Piece"""
    name = 'Queen'

    def __init__(self, colour):
        super().__init__(colour)

    def check_available(self):
        self.available = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not self.board.check_border((chr(ord(self.position[0]) + i), self.position[1] + j)):
                    c = (chr(ord(self.position[0]) + i), self.position[1] + j)
                    while self.board.piece(c).name == '-':
                        self.available.append(c)
                        if not self.board.check_border((chr(ord(c[0]) + i), c[1] + j)):
                            c = (chr(ord(c[0]) + i), c[1] + j)
                        else:
                            break
                    if self.board.piece(c).colour != self.colour and self.board.piece(c).colour != '':
                        self.available.append(c)


class king(piece):
    """King Piece"""
    name = 'King'

    def __init__(self, colour):
        super().__init__(colour)

    def check_available(self):
        self.available = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not self.board.check_border((chr(ord(self.position[0]) + i), self.position[1] + j)):
                    c = (chr(ord(self.position[0]) + i), self.position[1] + j)
                    if self.board.piece(c).name == '-' or self.board.piece(c).colour != self.colour:
                        self.available.append(c)
