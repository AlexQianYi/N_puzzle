#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:18:18 2018

@author: yiqian
"""
import copy
import math

class table:
    
    def __init__(self, input_table, N):
        self.table = copy.deecopy(input_table)
        
        self.step_path = []
        self.score = 0
        self.n = N
        
    def find(self, tile, table):
        blank_x, blank_y = 0,0
        for i in range(self.n):
            for j in range(self.n):
                if table[i][j]==tile:
                    blank_x, blank_y=i, j
        return blank_x, blank_y
        
    def move(self, action):
        print('move')
        blank_x, blank_y = self.find(0, self.table)
    
        if action=='u':
            y,x = 1,0
        if action=='d':
            y,x = -1,0
        if action=='l':
            y,x = 0,1
        if action=='r':
            y,x = 0,-1
        
        if blank_y+y not in range(0, self.n):
            return False
        if blank_x+x not in range(0, self.n):
            return False
        
        temp_table = self.table[blank_x+x][blank_y+y]
        self.table[blank_x][blank_y] = temp_table
        self.table[blank_x+x][blank_y+y]=0
        
        return True
    
    def Manhattan(self, goal_state):
        
        sum = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.state[i][j]==0:
                    continue
                else:
                    sum += self.ManhattanDis(self.state[i][j], (i,j), goal_state)
                    
        return sum
    
    def ManhattanDis(self, tile, position, goal_state):
        
        blank_x, blank_y = self.find(tile, goal_state)
        
        distance = (abs(position[0]-blank_x) + abs(position[1]-blank_y))
        
        return distance