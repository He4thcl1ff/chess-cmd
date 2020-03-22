from board import *
from piece import *
import copy


def standard():
    b1 = board(8)
    colours = ('W', 'B')
    for j in range(2):
        for i in range(8):
            b1.set_piece(pawn(colours[j]), (chr(65 + i), 2 + j * 5))
        for k in range(2):
            b1.set_piece(rook(colours[j]), (chr(65 + k * 7), 1 + j * 7))
            b1.set_piece(knight(colours[j]), (chr(66 + k * 5), 1 + j * 7))
            b1.set_piece(bishop(colours[j]), (chr(67 + k * 3), 1 + j * 7))
        b1.set_piece(queen(colours[j]), (chr(68), 1 + j * 7))
        b1.set_piece(king(colours[j]), (chr(69), 1 + j * 7))
    b1.update()

    # setup complete

    turn = 0
    while 1:
        turn += 1
        backup = copy.deepcopy(b1.status)
        if b1.check[0]:
            print('\n' + 'Player', colours[(turn + 1) % 2], 'is in Check!')
        b1.print_status(b1.status)
        print('Turn:', turn, '\n' + 'Player:', colours[(turn + 1) % 2], '\n')
        x, y = input('From:'), input('To:')
        if b1.piece((x[0], int(x[1]))).colour != colours[(turn + 1) % 2]:
            turn -= 1
            print('\n' + 'It is not your turn!')
        else:
            if not b1.move((x[0], int(x[1])), (y[0], int(y[1]))):
                turn -= 1
                print('\n' + 'Not able to move on that field!')
            else:
                b1.move((x[0], int(x[1])), (y[0], int(y[1])))
                if b1.check[0] and b1.check[1] != colours[(turn + 1) % 2]:
                    turn -= 1
                    print('\n' + 'You are not allowed to move into Check!')
                    b1.status = backup
                    b1.update()

    # game loop


standard()
