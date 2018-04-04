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
import sys
sys.setrecursionlimit(1000000)

step_seq = []


class Node:
    def __init__(self, table, score, parent, children, move, last_action):
        self.table = table
        self.score = score
        self.parent = parent
        self.children = children
        self.move = move
        self.visit = 1
        self.last_action = last_action
        

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
    print('move')
    blank_x, blank_y = 0,0
    for i in range(N):
        for j in range(N):
            if table[i][j]==0:
                blank_x, blank_y=i, j
                
    temp_table = []
    for i in range(N):
        temp_table.append([])
        for j in range(N):
            temp_table[i].append(table[i][j])
    
    if action=='u':
        temp_table[blank_x][blank_y]=temp_table[blank_x+1][blank_y]
        temp_table[blank_x+1][blank_y]=0
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
        
    
def move_check(last_action, current_action):
    if last_action=='u' and current_action=='d':
        return True
    if last_action=='d' and current_action=='u':
        return True
    if last_action=='r' and current_action=='l':
        return True
    if last_action=='l' and current_action=='r':
        return True
    return False

def nextStep(current_table, N):
    print('nextstep')
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
            next_state.append(['left', 'l'])
            return next_state
        if blank_y==(N-1):
            next_state.append(['up', 'u'])
            next_state.append(['down', 'd'])
            next_state.append(['right', 'r'])
            return next_state
            
    if blank_y>0 and blank_y<N-1:
        if blank_x==0:
            next_state.append(['up', 'u'])
            next_state.append(['left', 'l'])
            next_state.append(['right', 'r'])
            return next_state
        if blank_x==(N-1):
            next_state.append(['down', 'd'])
            next_state.append(['left', 'l'])
            next_state.append(['right', 'r'])
            return next_state
    
    if blank_x==0:
        if blank_y==0:
            next_state.append(['up', 'u'])
            next_state.append(['left', 'l'])
            return next_state
        if blank_y==(N-1):
            next_state.append(['up', 'u'])
            next_state.append(['right', 'r'])
            return next_state
    
    if blank_x==(N-1):
        if blank_y==0:
            next_state.append(['down', 'd'])
            next_state.append(['left', 'l'])
            return next_state
        if blank_y==(N-1):
            next_state.append(['down', 'd'])
            next_state.append(['right', 'r'])
            return next_state

      
def run(node, N, target, step_count, deep):
    print('run')
    print(node.table)
    global step_seq
    if deep==-1:
        return 
    if step_count ==20:
        return 
        
    if node.table==target:
        return 
    elif len(node.move)==0 and node.visit==0:
        run(node.parent, N, target, step_count+1, deep-1)
    elif len(node.move)!=0:
        temp_min_score = 100
        temp_next_node = None
        next_step = 'u'
        node.children = []
        for i in range(len(node.move)):
            temp_table = move(node.table, node.move[i], N)
            temp_score = manhattan(temp_table)
            children_node = Node(temp_table, temp_score, node, [], [], node.move[i])
            children_node.visit = 0
            node.children.append(children_node)
            if temp_score<temp_min_score:
                temp_min_score = temp_score
                temp_next_node = children_node
                next_step = node.move[i]
        if temp_min_score!=100:
            node.move.remove(next_step)
            print(next_step)
            run(temp_next_node, N, target, step_count+1, deep+1)
        else:
            run(node.parent, N, target, step_count+1, deep-1)
            
    else:
        next_state = nextStep(node.table, N)
        temp_min_score = 100
        temp_next_node = None
        next_step = 'u'
        print(deep)
        for i in range(len(next_state)):
            if move_check(node.last_action, next_state[i][1]):
                continue
            else:
                temp_table = move(node.table, next_state[i][1], N)
                temp_score = manhattan(temp_table)
                children_node = Node(temp_table, temp_score, node, [], [], next_state[i][1])
                children_node.visit=0
                node.children.append(children_node)
                node.move.append(next_state[i][1])
                if temp_score<temp_min_score:
                    temp_min_score=temp_score
                    temp_next_node = children_node
                    next_step = next_state[i][1]
        if temp_min_score!=100:
            node.move.remove(next_step)
            print(next_step)
            run(temp_next_node, N, target, step_count+1, deep+1)
        else:
            run(node.parent, N, target, step_count+1, deep-1)
            
            
            

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
    
    root = Node(table_ini, score, None, [], [], None)
    
        
    if root.table==target:
        print('done') 
    else:
        next_state = nextStep(root.table, N)
        temp_min_score = 100
        temp_next_node = None
        next_step = 'u'
        for i in range(len(next_state)):
            temp_table = move(root.table, next_state[i][1], N)
            temp_score = manhattan(temp_table)
            children_node = Node(temp_table, temp_score, root, [], [], next_state[i][1])
            root.children.append(children_node)
            root.move.append(next_state[i][1])
            if temp_score<temp_min_score:
                temp_min_score=temp_score
                temp_next_node = children_node
                next_step = next_state[i][1]
        if temp_min_score!=100:
            root.move.remove(next_step)
            root.visit = 0            
            run(temp_next_node, N, target, 1, 0)
            
    print(step_seq)           
    
    