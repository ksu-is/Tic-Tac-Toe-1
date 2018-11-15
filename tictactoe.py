"""tictactoe game for 2 players
from blogpost: http://thebillington.co.uk/blog/posts/writing-a-tic-tac-toe-game-in-python by  BILLY REBECCHI,
slightly improved by Horst JENS"""
from __future__ import print_function

choices = []

for x in range (0, 9) :
    choices.append(str(x + 1))
    print("Lets play Tic-Tac-Toe!")
player_1_pick = ""
player_2_pick = ""
player_1 = input("Enter a name for player 1 and press enter, leave blank to leave as Player 1: ")
player_2 = input("Enter a name for player 2 and press enter, leave blank to leave as Player 2: ")


if (player_1 == "" or player_2 == ""):
  if (player_1 == ""):
    player_1 = "Player 1"
  if (player_2 == ""):
    player_2 = "Player 2"
else:
  pass

playerOneTurn = True
winner = False

def printBoard() :
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')

while not winner :
    printBoard()

    if playerOneTurn :
        print( player_1 )
    else :
        print( player_2 )
    try:
        choice = int(input(">> "))
    except:
        print("please enter a valid field")
        continue
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        print("illegal move, plase try again")
        continue

    if playerOneTurn:
    
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " Congratulations on your win!\n")
