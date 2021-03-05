# -*- coding: utf-8 -*-
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
                if(self.space in [28,20,12,4]):
                    return [self.space+4]
                elif self.space in[29,21,13,5]:
                    return [self.space+4]
                else:
                    return [self.space+3,self.space+4]
            elif self.king:
                if(self.space in [28,20,12,4]):
                    return [self.space+4,self.space-4]
                elif self.space in[29,21,13,5]:
                    return [self.space+4,self.space-4]
                else:
                    return [self.space+3,self.space+4,self.space-3,self.space-4]
            if self.color=='w' and not self.king:
                if(self.space in [28,20,12,4]):
                    return [self.space-4]
                elif self.space in[29,21,13,5]:
                    return [self.space-4]
                else:
                    return [self.space-4,self.space-5]
            elif self.king:
                if(self.space in [28,20,12,4]):
                    return [self.space+4,self.space-4]
                elif self.space in[29,21,13,5]:
                    return [self.space+4,self.space-4]
                else:
                    return [self.space+4,self.space+5,self.space-4,self.space-5]
        else:
            if self.color=='b' and not self.king:
                if(self.space in [28,20,12,4]):
                    return [self.space+4]
                elif self.space in[29,21,13,5]:
                    return [self.space+4]
                else:
                    return [self.space+4,self.space+5]
            elif self.king:
                if(self.space in [28,20,12,4]):
                    return [self.space+4,self.space-4]
                elif self.space in[29,21,13,5]:
                    return [self.space+4,self.space-4]
                else:
                    return [self.space+4,self.space+5,self.space-4,self.space-5]
            if self.color=='w' and not self.king:
                if(self.space in [28,20,12,4]):
                    return [self.space-4]
                elif self.space in[29,21,13,5]:
                    return [self.space-4]
                else:
                    return [self.space-3,self.space-4]
            elif self.king:
                if(self.space in [28,20,12,4]):
                    return [self.space+4,self.space-4]
                elif self.space in[29,21,13,5]:
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

    
    
if __name__ == '__main__':
    p=[ piece(x,0) for x in range(0,32)]
    for x in range(1,13):
        p[-x]=piece(x,"b")
    for x in range(21,33):
        p[-x]=piece(x,"w")

    def drawP(board):
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

    #print(p[11])

    drawP(p)
    
