# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:14:09 2021

@author: Jake
"""

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
    mv=input("Enter move in format(11-15): ")
    
    move=mv.split("-")
    
    #if it is player 1's turn, check if the piece is black and the resulting place is empty
    if turn==0:
        if board[-int(move[1])]==0 and board[-int(move[0])]=='b':
            board[-int(move[1])]=board[-int(move[0])]
            board[-int(move[0])]=0
            return board
        else:
            print("Invalid move.")
            return makeMove(board,turn)
    #if it is player 2's turn, check if the piece is white and the resulting place is empty
    else:
        if board[-int(move[1])]==0 and board[-int(move[0])]=='w':
            board[-int(move[1])]=board[-int(move[0])]
            board[-int(move[0])]=0
            return board
        else:
            print("Invalid move.")
            return makeMove(board,turn)


#Print the current board
def drawB(board):
    #change the board into an array of arrays that represent the rows of the board
    bb=np.reshape(board,(-1,4))
    count=0
    
    #loop through the rows
    for i in bb:
    #loop through the elements of the rows
        for j in range(0,len(i)):
            #if it is an even row, print a space before each piece
            if count==0:
                print(' ',end='')
                print(i[j],end='')
            #if it is an odd row, print a space after each piece
            else:
                print(i[j],end='')
                print(' ',end='')
        #after each row, print a new line
        print()
        #then change the row to the opposite type(odd or even)
        if count==0:
            count+=1
        else:
            count-=1
            
        
        

#Initialize the board with values of 0 for 32 spaces
lboard=[ 0 for x in range(0,32)]

#set the first 12 spaces to white
for i in range(0,12):
    lboard[i]='w'
#set the last 12 spaces to black
for i in range(20,32):
    lboard[i]='b'

#initialize the turn as 0
turn=0

#start the game loop
while True:

    #Print the board
    drawB(lboard)
    
    #ask for a move
    lboard=makeMove(lboard,turn)


    #Change the turn to the next player's turn
    if turn==0:
        turn=1
    else:
        turn=0
        
    #Formatting print statements
    print()
    print('-'*10)
    print()
    #Ask if the game should end
    if input("Continue playing?(0 to quit)")=='0':
        break
    #Formatting print statements
    print()
    print('-'*10)
    print()
