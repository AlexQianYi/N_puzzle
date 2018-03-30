#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 19:49:14 2018

@author: yiqian
"""
"""
1 2 3
4 5 6
7 8
"""
N = 3

class Node:
    def __init__(N, table, score, parent):
        self.table = table
        self.N = N
        self.score = score
        self.parent = parent
        
        

def hamming(table):
    global N
    count_hamming=0
    for i in range(N):
        for j in range(N):
            temp = i*N+j+1
            if table[i][j]==temp:
                count_hamming+=1
    return count_hamming

def manhattan(table):
    global N
    count_manhattan=0
    for i in range(N):
        for j in range(N):
            goal_x=table[i][j]/N
            goal_y=(table[i][j]-1)%N
            if goal_x==i and goal_y==j:
                count_manhattan+=1
    return count_manhattan

def nextStep(current_table):
    global N
    next_state = []
    blank_x, blank_y = 0, 0
    
    for i in range(N):
        for j in range(N):
            if current_table[i][j]==0:
                blank_x, blank_y = i,j
                break
            
    if blank_x>0 and blank_x<N-1 and blank_y>0 and blank_y<N-1:
        next_state.append(['up', 'u'])
        next_state.append(['down', 'd'])
        next_state.append(['left', 'l'])
        next_state.append(['right', 'r'])
        return next_state
    
    if blank_x>0 and blank_x<N-1:
        if blank_y==0:
            next_state.append(['up', 'u'])
            next_state.append(['down', 'd'])
            next_state.append(['right', 'r'])
            return next_state
        if blank_y==(N-1):
            next_state.append(['up', 'u'])
            next_state.append(['down', 'd'])
            next_state.append(['left', 'l'])
            return next_state
            
    if blank_y>0 and blank_y<N-1:
        if blank_x==0:
            next_state.append(['down', 'd'])
            next_state.append(['left', 'l'])
            next_state.append(['right', 'r'])
            return next_state
        if blank_x==(N-1):
            next_state.append(['up', 'u'])
            next_state.append(['left', 'l'])
            next_state.append(['right', 'r'])
            return next_state
    
    if blank_x==0:
        if blank_y==0:
            next_state.append(['down', 'd'])
            next_state.append(['right', 'r'])
            return next_state
        if blank_y==(N-1):
            next_state.append(['down', 'd'])
            next_state.append(['left', 'l'])
            return next_state
    
    if blank_x==(N-1):
        if blank_y==0:
            next_state.append(['up', 'u'])
            next_state.append(['right', 'r'])
            return next_state
        if blank_y==(N-1):
            next_state.append(['up', 'u'])
            next_state.append(['left', 'l'])
            return next_state

"""        
def run(table, N, Node):
    if Node.table
"""
            

if __name__=='__main__':
    f = open('n-puzzle.txt', 'r')
    result = list()
    
    for line in open('n-puzzle.txt'):
        line = f.readline()
        print(line)
        result.append(line)
    print(result)
    f.close()
            
            
    