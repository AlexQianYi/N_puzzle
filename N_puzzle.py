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


class Node:
    def __init__(self, table, score, parent, children):
        self.table = table
        self.score = score
        self.parent = parent
        self.children = children
        

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

def move(table, action, N):
    blank_x, blank_y = 0,0
    for i in range(N):
        for j in range(N):
            if table[i][j]==0:
                blank_x, blank_y=i, j
    
    if action=='u':
        table[blank_x][blank_y]=table[blank_x+1][blank_y]
        table[blank_x+1][blank_y]=0
        return table
    if action=='d':
        table[blank_x][blank_y]=table[blank_x-1][blank_y]
        table[blank_x-1][blank_y]=0
        return table
    if action=='l':
        table[blank_x][blank_y]=table[blank_x][blank_y+1]
        table[blank_x][blank_y+1]=0
        return table
    if action=='r':
        table[blank_x][blank_y]=table[blank_x][blank_y-1]
        table[blank_x][blank_y-1]=0
        return table
        

def nextStep(current_table, N):
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

      
def run(node, N, target, step_count, deep, step_seq):
    if node.table==target:
        return 
    else:
        next_state = nextStep(node.table, N)
        temp_min_score = 100
        temp_next_node = None
        next_step = 'u'
        for i in range(len(next_state)):
            temp_table = move(node.table, next_state[i][1], N)
            temp_score = manhattan(temp_table)
            children_node = Node(temp_table, temp_score, node, [])
            node.children.append(children_node)
            if temp_score<temp_min_score:
                temp_min_score=temp_score
                temp_next_node = children_node
                next_step = next_state[i][1]
        run(temp_next_node, N, target, step_count+1, deep+1, step_seq.append(next_step))
            
            
            

if __name__=='__main__':
    f = open('n-puzzle.txt', 'r')
    result = list()
    table_ini = []
    k=0
    for line in open('n-puzzle.txt'):
        line = f.readline()
        table_ini.append([])
        for i in range(len(line)):
            if line[i]!='\t' and line[i]!='\n':
                table_ini[k].append(int(line[i]))
        result.append(line)
        k+=1
    print(table_ini)
    f.close()
    
    N = len(table_ini[0])
    target = [[j for j in range(1+i*N, (i+1)*N+1)] for i in range(N)]
    target[-1][-1]=0
    print(target)
    score = manhattan(table_ini)
    
    root = Node(table_ini, score, None, [])
    step_count, step_seq, deep = 0, [], 0
    
    run(root, N, target, step_count, deep, step_seq)
            
    print(step_count)
    print(step_seq)           
    
    