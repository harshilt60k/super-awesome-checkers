"""
Created on Fri Feb 19 13:19:54 2021

@author: Jake
"""
import numpy as np
class piece():
    def __init__(self,space,color):
        self.space=space
        self.king=False
        self.color=color
        
    def setRow(self,row):
        self.row=row
    
    def posMoves(self):

        if self.row in [0,2,4,6]:
            if self.color=='b' and not self.king:
                if(self.space in [28,20,12,4,29,21,13,5]):
                    return [self.space+4]
                else:
                    return [self.space+3,self.space+4]
            elif self.king:
                if(self.space in [28,20,12,4,29,21,13,5]):
                    return [self.space+4,self.space-4]
                else:
                    return [self.space+3,self.space+4,self.space-3,self.space-4]
            if self.color=='w' and not self.king:
                if(self.space in [28,20,12,4,29,21,13,5]):
                    return [self.space-4]
                else:
                    return [self.space-4,self.space-5]
            elif self.king:
                if(self.space in [28,20,12,4,29,21,13,5]):
                    return [self.space+4,self.space-4]
                else:
                    return [self.space+4,self.space+5,self.space-4,self.space-5]
        else:
            if self.color=='b' and not self.king:
                if(self.space in [28,20,12,4,29,21,13,5]):
                    return [self.space+4]
                else:
                    return [self.space+4,self.space+5]
            elif self.king:
                if(self.space in [28,20,12,4,29,21,13,5]):
                    return [self.space+4,self.space-4]
                else:
                    return [self.space+4,self.space+5,self.space-4,self.space-5]
            if self.color=='w' and not self.king:
                if(self.space in [28,20,12,4,29,21,13,5]):
                    return [self.space-4]
                else:
                    return [self.space-3,self.space-4]
            elif self.king:
                if(self.space in [28,20,12,4,29,21,13,5]):
                    return [self.space+4,self.space-4]
                else:
                    return [self.space+3,self.space+4,self.space-3,self.space-4] 
            
    def checkJump(self,board):
        moves=self.posMoves()
        color = self.getColor()
        if color =='b':
            opposite='w'
        else:
            opposite='b'    
        if self.king:
            if self.space in [28,20,12,4] or self.space in [29,21,13,5]:
                if opposite == 'w':
                    if board[-int(moves[0])].getColor()==opposite:
                        if board[-int(self.space+9)].getColor()==0:
                            return [True,self.space+9]
                    if board[-int(moves[-1])].getColor()==opposite:
                        if board[-int(self.space+7)].getColor()==0:
                            return [True,self.space+7]
                else:
                    if board[-int(moves[0])].getColor()==opposite:
                        if board[-int(self.space-9)].getColor()==0:
                            return [True,self.space-9]
                    if board[-int(moves[-1])].getColor()==opposite:
                        if board[-int(self.space-7)].getColor()==0:
                            return [True,self.space-7]
            else:
                if opposite == 'w':
                    if board[-int(moves[0])].getColor()==opposite:
                        if board[-int(self.space+7)].getColor()==0:
                            return [True,self.space+7]
                    if board[-int(moves[-1])].getColor()==opposite:
                        if board[-int(self.space+9)].getColor()==0:
                            return [True,self.space+9]
                else:
                    if board[-int(moves[0])].getColor()==opposite:
                        if board[-int(self.space-7)].getColor()==0:
                            return [True,self.space-7]
                    if board[-int(moves[-1])].getColor()==opposite:
                        if board[-int(self.space-9)].getColor()==0:
                            return [True,self.space-9]
        else:
            if self.space in [28,20,12,4] or self.space in [29,21,13,5]:
                if opposite == 'w':
                    if board[-int(moves[0])].getColor()==opposite:
                        if board[-int(self.space+9)].getColor()==0:
                            return [True,self.space+9]
                    if board[-int(moves[-1])].getColor()==opposite:
                        if board[-int(self.space+7)].getColor()==0:
                            return [True,self.space+7]
                else:
                    if board[-int(moves[0])].getColor()==opposite:
                        if board[-int(self.space-9)].getColor()==0:
                            return [True,self.space-9]
                    if board[-int(moves[-1])].getColor()==opposite:
                        if board[-int(self.space-7)].getColor()==0:
                            return [True,self.space-7]
            else:
                if opposite == 'w':
                    if board[-int(moves[0])].getColor()==opposite:
                        if board[-int(self.space+7)].getColor()==0:
                            return [True,self.space+7]
                    if board[-int(moves[-1])].getColor()==opposite:
                        if board[-int(self.space+9)].getColor()==0:
                            return [True,self.space+9]
                else:
                    if board[-int(moves[0])].getColor()==opposite:
                        if board[-int(self.space-7)].getColor()==0:
                            return [True,self.space-7]
                    if board[-int(moves[-1])].getColor()==opposite:
                        if board[-int(self.space-9)].getColor()==0:
                            return [True,self.space-9]
        
    def getSpace(self):
        return self.space
    
    def getColor(self):
        return self.color
    
    def changeSpace(self,space):
        self.space=space
    def isKing(self):
        if self.king==True:
            return True
        return False
    
    def checkPromote(self):
        if self.space in [32,31,30,29] and self.color=="b":
            self.king=True
        
class board():
    def __init__(self):
        self.board=[ piece(x,0) for x in range(0,32)]
        for x in range(1,13):
            self.board[-x]=piece(x,"b")
        for x in range(21,33):
            self.board[-x]=piece(x,"w")
        
    def drawP(self):
    #change the board into an array of arrays that represent the rows of the board
        board=self.board
        bb=np.reshape(board,(-1,4))
        count=0
        rCount=0    
        #loop through the rows
        for i in bb:
            #loop through the elements of the rows
            for j in range(0,len(i)):
                i[j].setRow(rCount)
                i[j].checkPromote()
                #if it is an even row, print a space before each piece
                if count==0:
                    print(' ',end='')
                    color =i[j].getColor() if not i[j].king else i[j].getColor().upper()
                    print(color,end='')
                    #if it is an odd row, print a space after each piece
                else:
                    color =i[j].getColor() if not i[j].king else i[j].getColor().upper()
                    print(color,end='')
                    print(' ',end='')
                    #after each row, print a new line
            print()
        #then change the row to the opposite type(odd or even)
            if count==0:
                count+=1
            else:
                count-=1
            rCount+=1
#In order to count the number of pieces on the board at the current time in the game
    def piecesleft(self):
        self.blacks=0
        self.whites=0
        self.whiteK=0
        self.blackK=0
        for i in self.board:
            if i.color=="b":
                self.blacks+=1
            elif i.color=="w":
                self.whites+=1
            if  i.isKing==True and i.color=="w":
                self.whiteK+=1
            elif  i.isKing==True and i.color=="b":
                self.blackK+=1
#get all the pieces based on the color
    def getAllPieces(self, color):
        pieces=[]
        for piece in self.board:
            if piece!=0 and piece.color==color:
                pieces.append(piece)
        return pieces
#check winner
    def checkWinner(self):
        if self.blacks<=0:
            return "white"
        elif self.whites<=0:
            return "black"
        return None
    
# test from youtube video  
    def evaluate(self):
        return self.whites - self.blacks + (self.whiteK * 0.5 - self.blackK * 0.5)