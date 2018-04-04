#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 11:15:55 2018

@author: yiqian
"""
import GameTreeNode

priority_queue = []

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
    
    root = GameTreeNode(table_ini, None, )
    
    priority_queue.append(root)
    
    while(!)
    
        
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