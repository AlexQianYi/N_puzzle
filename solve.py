#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:02:22 2018

@author: yiqian
"""

import utility
import copy
import environment
import table


class solve:
    
    def __init__(self, input_table):
        
        self.initial_state = copy.deepcopy(input_table)       
        self.goal_state = self.SetGoalState(input_table)      
        self.AStarQueue = utility.PriorityQueue()
        self.explored = utility.Explored()
        self.frontier = utility.Frontier()
        
        self.env = environment.environment(self.frontier)
        
    def AStarSearch(self):
        print('A star')
        
        self.env.StartTime()
        
        n = len(self.initial_state)
        
        init_table = table.Table(self.initial_state, n)
        init_score = init_table.Manhattan(self.goal_state)
        
        self.AStarQueue.queue.put((init_score, init_table))
        c = 0
        
        while self.AStarQueue.queue:
            print(c)
            #if c==20:
             #   break
            
            min_score = self.AStarQueue.queue.get()
            state = min_score[1]
            
            self.env.search_deep = len(state.path_history)
            self.env.UpdateDeep()
            
            not_find = 0
            for i in range(len(self.explored.set)):
                if self.explored.set[i]==state.table:
                    not_find = 1
                    break
            if not_find == 0:
                self.explored.set.append(state.table)
            
            if self.GoalTest(state):
                self.env.path = state.path_history
                self.env.StopTime()
                print(state.table)
                return self.env
            
            self.ExpandNode(state)
            c+=1
            
        print("Error")
        
    def ExpandNode(self, start_table):
            
        action = ['u', 'd', 'l', 'r']
        
        n = len(self.initial_state)
            
        for act in action:
                
            temp_table = table.Table(start_table.table, n)
                
            temp_table.path_history = copy.copy(start_table.path_history)
                
            if temp_table.move(act):
                temp_table.path_history.append(act)
                    
                if temp_table not in self.frontier and temp_table.table not in self.explored.set:
                    temp_table.score = temp_table.Manhattan(self.goal_state)
                    self.AStarQueue.queue.put((temp_table.score, temp_table))
                        
                self.env.UpdateQueue()
                    
            self.env.node_expanded +=1
            
    def GoalTest(self, state):
        if state.table == self.goal_state:
            return True
        else:
            return False
        
    def SetGoalState(self, input_list):
        
        n = int(len(input_list))
        goal_state = [['-' for x in range(n)] for y in range(n)]
        
        i,j = 0, 0
        count = 1
        
        while i<n:
            if count == n*n:
                count=0
            goal_state[i][j] =count
            count+=1
            j +=1
            if j==n:
                j=0
                i+=1
        return goal_state
    
    
                
                