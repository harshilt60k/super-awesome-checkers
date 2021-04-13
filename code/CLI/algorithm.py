# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:00:00 WAT 2021

@author: Ayomide
"""
from copy import deepcopy
from setup import piece, board
#This is to evaluate moves from the minimax AI and test out those moves sfrom the Simulate move function 
def AImove(board,start,stop, isJump=False,opposite=None):
    if isJump:
        board[-int(stop)]=board[-int(start)]
        board[-int(stop)].changeSpace(int(stop))
        board[-int(start)]=piece(int(start),0)
        board[-int(opposite)]=piece(int(start),0)
        return board
    if board[-int(stop)].color==0:
        board[-int(stop)]=board[-int(start)]
        board[-int(stop)].changeSpace(int(stop))
        board[-int(start)]=piece(int(start),0)
    
    return board
    
def minimax(position,depth,max_player):
    #checks if the depth is greater than zero and that no one has won the game yet
    if depth ==0 or position.checkWinner()!=None:
        return position.evaluate(),position
    #checks that the max player is set, and is always set to white as we would want to play with the White as the AI
    if max_player:
        maxEval = float('-inf')
        best_move=None
        #checks each move outlined in the get_all_moves function then recursively runs this function again and again until the deptth is zero
        for move in get_all_moves(position,"w"):
            evaluation=minimax(move,depth-1,False)[0]
            maxEval=max(maxEval,evaluation)
            if maxEval==evaluation:
                best_move=move
        return maxEval,best_move
    else:
        minEval = float('inf')
        best_move=None
        for move in get_all_moves(position,"b"):
            evaluation=minimax(move,depth-1,True)[0]
            minEval=min(minEval,evaluation)
            if minEval==evaluation:
                best_move=move
        return minEval,best_move
        
#runs possible move on a copy of the currentt board in the game
def simulate_move(piece,move,board,isJump=False,opposite=None):
    if isJump:
        AImove(board.board,piece.space,move,isJump=True,opposite=opposite)
        return board
    AImove(board.board,piece.space,move)
    return board
    
#This gets and checks all possible moves for all the pieces of the same color on the board at any given time
def get_all_moves(board,color):
    moves=[]
    #Loops through all the piece objects that are of that color
    for piece in board.getAllPieces(color):
        valid_moves= piece.posMoves()
        jumps=None
        #checks if any jumps are possible for a specific piece at a given time and then appends that position to the valid_moves 
        if type(piece.checkJump(board.board))!=type(None):
            jumps=piece.checkJump(board.board)[1]
            valid_moves.append(jumps)
            oppositePos=piece.getOppositePos()
        #checks and simulates each move in the valid_moves list by crating an exact copy of the original board and then recursively applying the moves for the different pieces and testing the feasibility and then appending that possibility to a new list
        for move in range(len(valid_moves)):
            temp_board=deepcopy(board)
            if jumps==None:
                new_board=simulate_move(piece,valid_moves[move], temp_board)
            elif jumps!=None:
                new_board=simulate_move(piece,valid_moves[move], temp_board,isJump=True,opposite=oppositePos)
            moves.append(new_board)
        
    return moves