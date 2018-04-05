#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 11:57:41 2018

@author: yiqian
"""
import solve

if __name__=='__main__':
    f = open('n-puzzle.txt', 'r')
    result = list()
    table_ini = []
    k=0
    
    with open('n-puzzle.txt') as f:
        for line in f:
            table_ini.append([])
            for each in enumerate(line.split()):
                table_ini[k].append(int(each[1]))
            k+=1
    
    print(table_ini)
    f.close()
    
    N = len(table_ini[0])
    target = [[j for j in range(1+i*N, (i+1)*N+1)] for i in range(N)]
    target[-1][-1]=0
    
    
    
    solution = solve.solve(table_ini)
    result = solution.AStarSearch()
    
    
    print("initial state: "+ str(table_ini))
    print("path to goal: " + str(result.path))
    print("search deep: " + str(result.search_deep))
    print("running time: " + str(result.search_time)+"ms")
    print("number of node: "+ str(result.node_expanded))