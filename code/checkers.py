# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:14:09 2021

@author: Jake
"""
import piece
import numpy as np
'''
valid moves are index + 3,4,5 if black pieces
                index +/- 3,4,5 if black kings
                index - 3,4,5 if white pieces
                index +/- 3,4,5 if white kings

The following print statements find if it is a valid move for black or white

print((-int(move[1])+4==-int(move[0])) or (-int(move[1])+5==-int(move[0])) or (-int(move[1])+3==-int(move[0])))
print((-int(move[1])-4==-int(move[0])) or (-int(move[1])-5==-int(move[0])) or (-int(move[1])-3==-int(move[0])))
'''



#Function that changes position on the board
def makeMove(board,turn):
    #take the move as an input
    mv=input("Enter move in format(11-15, 11x15 for jump): ")
    if 'x' in mv:
        move=mv.split("x")
        if board[-int(move[0])].checkJump(board)[0]:
            return makeJump(board,turn,move)
        else:
            print("Invalid jump.")
            return makeMove(board, turn)
    move=mv.split("-")
    #use to check the movements of players since the table's outlook does not change
    #possiblePositions = possibleMovements(move,board)
    #print(move)
    #print(board[-int(move[0])].posMoves())
    #print(move)
    #if it is player 1's turn, check if the piece is black and the resulting place is empty
    if turn==0:
        #Upgrade piece to king, "kb" signifies a promoted piece -Ayo
        if board[-int(move[1])].color==0 and board[-int(move[0])].color=='b' and int(move[1]) in board[-int(move[0])].posMoves():
            board[-int(move[1])]=board[-int(move[0])]
            board[-int(move[1])].changeSpace(int(move[1]))
            board[-int(move[0])]=piece.piece(int(move[0]),0)
            return board
        else:
            print("Invalid move.")
            return makeMove(board,turn)
    #if it is player 2's turn, check if the piece is white and the resulting place is empty
    else:
        #Promote piece to king, "kw" signifies a promoted piece -Ayo
        if board[-int(move[1])].color==0 and board[-int(move[0])].color=='w' and (int(move[1]) in board[-int(move[0])].posMoves()) :
            board[-int(move[1])]=board[-int(move[0])]
            board[-int(move[1])].changeSpace(int(move[1]))
            board[-int(move[0])]=piece.piece(int(move[0]),0)
            return board
        else:
            print("Invalid move.")
            return makeMove(board,turn)

def makeJump(board, turn, move):
    #take the move as an input
    finalLocation=board[-int(move[0])].checkJump(board)[1]
    
    #print(move)
    #print(finalLocation)
    board[-int(finalLocation)]=board[-int(move[0])]
    board[-int(finalLocation)].changeSpace(int(finalLocation))
    board[-int(move[0])]=piece.piece(int(move[0]),0)
    board[-int(move[1])]=piece.piece(int(move[0]),0)
    return board
        
        
    
        
        
def drawP(board):
    #change the board into an array of arrays that represent the rows of the board
    bb=np.reshape(board,(-1,4))
    count=0
    rCount=0    
    #loop through the rows
    for i in bb:
        #loop through the elements of the rows
        for j in range(0,len(i)):
            i[j].setRow(rCount)
            #if it is an even row, print a space before each piece
            if count==0:
                print(' ',end='')
                print(i[j].getColor(),end='')
                #if it is an odd row, print a space after each piece
            else:
                print(i[j].getColor(),end='')
                print(' ',end='')
                #after each row, print a new line
        print()
    #then change the row to the opposite type(odd or even)
        if count==0:
            count+=1
        else:
            count-=1
        rCount+=1
#Initialize the board with values of 0 for 32 spaces

p=[ piece.piece(x,0) for x in range(0,32)]
for x in range(1,13):
    p[-x]=piece.piece(x,"b")
for x in range(21,33):
    p[-x]=piece.piece(x,"w")


#initialize the turn as 0
turn=0

#start the game loop
while True:

    #Print the board
    drawP(p)
    
    #ask for a move
    p=makeMove(p,turn)

    #Formatting print statements
    print()
    print('-'*10)
    print()
    #Ask if the game should end
    if input("Continue playing?(q to quit)")=='q':
        break
    #Formatting print statements
    print()
    print('-'*10)
    print()
    
    #Change the turn to the next player's turn
    if turn==0:
        print("White's turn\n\n")
        turn=1
    else:
        print("Black's turn\n\n")
        turn=0
