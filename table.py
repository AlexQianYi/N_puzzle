#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:18:18 2018

@author: yiqian
"""
import copy

class table:
    
    def __init__(self, input_table, N):
        self.table = copy.deecopy(input_table)
        
        self.step_path = []
        self.score = 0
        self.n = N
        
    def blank(self, table):
        blank_x, blank_y = 0,0
        for i in range(self.n):
            for j in range(self.n):
                if table[i][j]==0:
                    blank_x, blank_y=i, j
        return blank_x, blank_y
        
    def move(self, action):
        print('move')
        blank_x, blank_y = self.blank(self.table)
    
        if action=='u':
            self.table[blank_x][blank_y]=self.table[blank_x+1][blank_y]
            self.table[blank_x+1][blank_y]=0
            return temp_table
        if action=='d':
            temp_table[blank_x][blank_y]=temp_table[blank_x-1][blank_y]
            temp_table[blank_x-1][blank_y]=0
            return temp_table
        if action=='l':
            temp_table[blank_x][blank_y]=temp_table[blank_x][blank_y+1]
            temp_table[blank_x][blank_y+1]=0
            return temp_table
        if action=='r':
            temp_table[blank_x][blank_y]=temp_table[blank_x][blank_y-1]
            temp_table[blank_x][blank_y-1]=0
            return temp_table