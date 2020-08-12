import sys


global player


def fnInit():
    return {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}


def fnPrintDictField(DictField):
    print(DictField['7'] + ' | ' + DictField['8'] + ' | ' + DictField['9'])
    print('--+---+--')
    print(DictField['4'] + ' | ' + DictField['5'] + ' | ' + DictField['6'])
    print('--+---+--')
    print(DictField['1'] + ' | ' + DictField['2'] + ' | ' + DictField['3'])


def fnSwapPlayer(player):
    if player == 'O': player = 'X'
    elif player == 'X': player = 'O'
    return player


def fnPlayerInput(player):
    try:
        print("Player " + str(player) + ": Take a field")
        playerInput = input()
        if fnCheckField(playerInput):
            DictField[playerInput] = str(player)
        else: fnPlayerInput(player)
    except KeyError:
        fnPlayerInput(player)


def fnCheckField(input):
    if DictField[input] == ' ': return True
    else: return False


def fnCheckForWinner(player, moves):
    win = False
    if DictField['7'] == DictField['8'] == DictField['9'] != ' ': # across the top
        win = True               
    elif DictField['4'] == DictField['5'] == DictField['6'] != ' ': # across the middle
        win = True
    elif DictField['1'] == DictField['2'] == DictField['3'] != ' ': # across the bottom
        win = True
    elif DictField['1'] == DictField['4'] == DictField['7'] != ' ': # down the left side
        win = True
    elif DictField['2'] == DictField['5'] == DictField['8'] != ' ': # down the middle
        win = True
    elif DictField['3'] == DictField['6'] == DictField['9'] != ' ': # down the right side
        win = True
    elif DictField['7'] == DictField['5'] == DictField['3'] != ' ': # diagonal
        win = True
    elif DictField['1'] == DictField['5'] == DictField['9'] != ' ': # diagonal
        win = True
    
    if win:
        fnPrintDictField(DictField)
        fnEndGame(True, player=player)
    else:
        if moves == 9:
            fnEndGame(False)


def fnEndGame(isWinner, player=None):
    if isWinner:
        print("\nGame Over.\n")                
        print(" **** " + player + " won. ****")
        fnPlayAgain()

    else:
        print("\nGame Over.\n")
        print("It's a tie")
        fnPlayAgain()


def fnPlayAgain():
    print("Do you want to play again? (Y)")
    userInput = input()
    if userInput == 'Y' or userInput == 'y':
        print("Thanks for playing again")
        game()
    else: 
        print("Thank you for playing")
        sys.exit(0)




def game():
    global DictField
    DictField = fnInit()
    player = 'O'
    for i in range(10):
        fnPrintDictField(DictField)
        player = fnSwapPlayer(player)
        fnPlayerInput(player)
        if i > 3:
            fnCheckForWinner(player, i)
            


       
        
        
if __name__ == "__main__":
    game()
