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
    
    solution = solve.Solve(table_ini)
    result = solution.a_star_search()