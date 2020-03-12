from board import *
from piece import *
import copy


def standard():
    b1 = board(8)
    colours = ['W', 'B']
    for j in range(2):
        for i in range(8):
            b1.set_piece(pawn(colours[j]), [chr(66 + j * 5), i])
        for k in range(2):
            b1.set_piece(rook(colours[j]), [chr(65 + j * 7), 1 + k * 7])
            b1.set_piece(knight(colours[j]), [chr(65 + j * 7), 2 + k * 5])
            b1.set_piece(bishop(colours[j]), [chr(65 + j * 7), 3 + k * 3])
        b1.set_piece(queen(colours[j]), [chr(65 + j * 7), 4])
        b1.set_piece(king(colours[j]), [chr(65 + j * 7), 5])
    b1.update()

    # setup complete

    turn = 0
    while 1:
        turn += 1
        backup = copy.deepcopy(b1.status)
        if b1.check[0]:
            print('\n' + 'Player', colours[(turn + 1) % 2], 'is in Check!')
        b1.print_status()
        print('Turn:', turn, '\n' + 'Player:', colours[(turn + 1) % 2], '\n')
        x, y = input(), input()
        if b1.piece([x[0], int(x[1])]).colour != colours[(turn + 1) % 2]:
            turn -= 1
            print('\n' + 'It is not your turn!')
        else:
            if not b1.move([x[0], int(x[1])], [y[0], int(y[1])]):
                turn -= 1
                print('\n' + 'Not able to move on that field!')
            else:
                b1.move([x[0], int(x[1])], [y[0], int(y[1])])
                b1.update()
                if b1.check[0] and b1.check[1] != colours[(turn + 1) % 2]:
                    turn -= 1
                    print('\n' + 'You are not allowed to move into Check!')
                    b1.status = backup
                    b1.update()

    # game loop


standard()
