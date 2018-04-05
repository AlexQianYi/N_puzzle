#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:18:18 2018

@author: yiqian
"""
import copy

class Table:
    
    def __init__(self, input_table, N):
        self.table = copy.deepcopy(input_table)
        
        self.path_history = list()
        self.score = 0
        self.n = N
        
    def __eq__(self, other):
        return self.score==other.score
    
    def __lt__(self, other):
        return self.score < other.score
        
    def find(self, tile, table):
        blank_x, blank_y = 0,0
        for i in range(self.n):
            for j in range(self.n):
                if table[i][j]==tile:
                    blank_x, blank_y=i, j
        return blank_x, blank_y
        
    def move(self, action):
        blank_x, blank_y = self.find(0, self.table)
    
        if action=='u':
            x,y = 1,0
        if action=='d':
            x,y = -1,0
        if action=='l':
            x,y = 0,1
        if action=='r':
            x,y = 0,-1
        
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
                if self.table[i][j]==0:
                    continue
                else:
                    sum += self.ManhattanDis(self.table[i][j], (i,j), goal_state)
                    
        return sum
    
    def ManhattanDis(self, tile, position, goal_state):
        
        blank_x, blank_y = self.find(tile, goal_state)
        
        distance = (abs(position[0]-blank_x) + abs(position[1]-blank_y))
        
        return distance
    
    def CheckRowCol(self, a, b):
        count = 0
        if b==100:
            for j in range(self.n):
                if self.table[a][j]==0:
                    continue
                temp_x = int(self.table[a][j]/self.n)
                temp_y = self.table[a][j]%self.n-1
                if temp_x==a and temp_y!=j:
                    count+=1
            if count>1:
                return count
            else:
                return 0
        if a==100:
            for i in range(self.n):
                if self.table[i][b]==0:
                    continue
                temp_x = int(self.table[i][b]/self.n)
                temp_y = self.table[i][b]%self.n-1
                if temp_y!=i and temp_x==b:
                    count+=1
            if count>1:
                return count
            else:
                return 0
    
    def Manhattan_LinearConflict(self, goal_state):
        
        sum = 0
        sum = self.Manhattan(goal_state)
        count = 0 
        
        for i in range(self.n):
            for j in range(self.n):
                if self.table[i][j]==0:
                    continue
                temp_x = int(self.table[i][j]/self.n)
                temp_y = self.table[i][j]%self.n-1
                # at goal row
                if temp_x == i and temp_y!=j:
                    count += self.CheckRowCol(temp_x, 100)
                    continue
                # at goal column
                if temp_x!=i and temp_y==j:
                    count += self.CheckRowCol(100, temp_y)
                    continue
        return sum+count