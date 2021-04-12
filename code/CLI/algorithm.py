from copy import deepcopy
from setup import piece, board
#This is to evaluate moves from the minimax AI 
def AImove(board,start,stop, isJump=False,opposite=None):
    if isJump:
        board[-int(stop)]=board[-int(start)]
        board[-int(stop)].changeSpace(int(stop))
        board[-int(start)]=piece(int(start),0)
        board[-int(opposite)]=piece(int(start),0)
        return board
    board[-int(stop)]=board[-int(start)]
    board[-int(stop)].changeSpace(int(stop))
    board[-int(start)]=piece(int(start),0)
    
    return board
    
def minimax(position,depth,max_player):
    if depth ==0 or position.checkWinner()!=None:
        return position.evaluate(),position
    if max_player:
        maxEval = float('-inf')
        best_move=None
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
            maxEval=min(minEval,evaluation)
            if maxEval==evaluation:
                best_move=move
        return maxEval,best_move
        

def simulate_move(piece,move,board,isJump=False,opposite=None):
    if isJump:
        AImove(board.board,piece.space,move,isJump=True,opposite=opposite)
        return board
    AImove(board.board,piece.space,move)
    return board
    
def get_all_moves(board,color):
    moves=[]
    
    for piece in board.getAllPieces(color):
        valid_moves= piece.posMoves()
        jumps=""
        if type(piece.checkJump(board.board))!=type(None):
            jumps=piece.checkJump(board.board)[1]
            valid_moves.append(jumps)
            oppositePos=piece.getOppositePos()
        for move in range(len(valid_moves)):
            temp_board=deepcopy(board)
            if jumps=="":
                new_board=simulate_move(piece,valid_moves[move], temp_board)
            elif jumps!="":
                new_board=simulate_move(piece,valid_moves[move], temp_board,isJump=True,opposite=oppositePos)
            moves.append(new_board)
    return moves