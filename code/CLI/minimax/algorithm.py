from copy import deepcopy

def minimax(position,depth,max_player,game):
    if depth ==0 or position.checkWinner()!=None:
        return position.eveluate(),position
    if max_player:
        maxEval = float('-inf')
        best_move=None
        for move in get_all_moves(position,"w"):
    else:
        pass


def get_all_moves(position,color,game):
    moves=[]
    for piece in board.get_all_piece(color):
        valid_moves=board.get
