#Cross Board game 423

import pprint
import random

theBoard = { 'topL' : ' ',
             'topM' : ' ',
             'topR' : ' ',
             'midL' : ' ',
             'midM' : ' ',
             'midR' : ' ',
             'botL' : ' ',
             'botM' : ' ',
             'botR' : ' ' }
    

#pprint.pprint(theBoard)


def display(board) :    ## Displaying the board
    print( '\n'+ board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print( '-----' )
    print( board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print( '-----' )
    print( board['botL'] + '|' + board['botM'] + '|' + board['botR'] + '\n')


def getPosition() :     ## Getting the correct position from user
    print('\nWhat is your move : ', end='')
    in_position = input()

    while in_position not in theBoard.keys() or theBoard[in_position] != ' ':
        print('Please enter the correct position')
        pprint.pprint(theBoard.keys())
        print("Your position : ", end='')
        in_position = input()

    theBoard[in_position] = 'O'



def computers_turn() :      ## Computers turn #dumb
    free_spots = []
    for a in theBoard.items():
        if a[1] == ' ' :
            free_spots.append(a[0])
            print('appended : ' + a[0])
    print( 'free ports list : ' + str(free_spots) )
    if len(free_spots) != 0 :
        theBoard[free_spots[random.randint(0,len(free_spots) - 1)]] = 'X'


def check_line(side) :
    if theBoard['topL'] == theBoard['topM'] == theBoard['topR'] == side or \
       theBoard['midL'] == theBoard['midM'] == theBoard['midR'] == side or \
       theBoard['botL'] == theBoard['botM'] == theBoard['botR'] == side or \
       theBoard['topL'] == theBoard['midL'] == theBoard['botL'] == side or \
       theBoard['topM'] == theBoard['midM'] == theBoard['botM'] == side or \
       theBoard['topR'] == theBoard['midR'] == theBoard['botR'] == side or \
       theBoard['topL'] == theBoard['midM'] == theBoard['botR'] == side or \
       theBoard['topR'] == theBoard['midM'] == theBoard['botL'] == side :
        return 1


'''def check(board, r) :      ## Check if won
    input_list = ''
    for a in theBoard.values() :
        if a == r :
            input_list += a
        else :
            input_list += ' '

    print('input list : ' + input_list)


    if r == 'O' :
        solution = ('OOO      ', '   OOO   ', '      OOO', 'O  O  O  ', ' O  O  O ', '  O  O  O', 'O   O  O ', '  O O   O')
        if input_list in solution :
            print('YOU WON')
            display(theBoard)
    else :
        solution = ('XXX      ', '   XXX   ', '      XXX', 'X  X  X  ', ' X  X  X ', '  X  X  X', 'X   X  X ', '  X X   X')
        if input_list in solution :
            print('Computer won')
            display(theBoard)
        '''
'''if input_list in sol_X :
        print('Computer won!')
        exit()
    elif input_list in sol_O :
        print('You beat Computer!')
        exit() ''' 
        
######################################
print("Computer is X")
display(theBoard)

no_turns = 0

while no_turns < 5 :
    getPosition()
    #check(theBoard,'O')
    if check_line('O'):
        print("You won")
        exit()
    computers_turn()
    #check(theBoard,'X')
    if check_line('X'):
        print("Comp won")
        exit()
    display(theBoard)

    no_turns += 1
