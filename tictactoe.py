"""tictactoe game for 2 players
from blogpost: http://thebillington.co.uk/blog/posts/writing-a-tic-tac-toe-game-in-python by  BILLY REBECCHI,
slightly improved by Horst JENS"""
from __future__ import print_function

choices = []

for x in range (0, 9) :
    choices.append(str(x + 1))
    print("Lets play Tic-Tac-Toe!")
Challenger_1_pick = ""
Challenger_2_pick = ""
Challenger_1 = input("Enter a name for Challenger 1 and press enter, leave blank to leave as Challenger 1: ")
Challenger_2 = input("Enter a name for Challenger 2 and press enter, leave blank to leave as Challenger 2: ")


if (Challenger_1 == "" or Challenger_2 == ""):
  if (Challenger_1 == ""):
    Challenger_1 = "Challenger 1"
  if (Challenger_2 == ""):
   Challenger_2 = "Challenger 2"
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
        print( Challenger_1 )
    else :
        print( Challenger_2 )
    try:
        choice = int(input(">> "))
    except:
        print("please enter a valid field")
        continue
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        print("illegal move, please try again")
        continue

    if playerOneTurn:
    
        choices[choice - 1] = '@'
    else :
        choices[choice - 1] = '%'

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

    print ("Challenger " + str(int(playerOneTurn + 1)) + " You Won !!!!!!!!!!!!WON!!!!!!!!!\n")
