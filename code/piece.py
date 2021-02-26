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
            
            
    def getColor(self):
        return self.color
    
    def changeSpace(self,space):
        self.space=space
