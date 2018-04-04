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
        
        self.env = environment.environment(self.AStarQueue)
        
    def AStarSearch(self):
        print('A star')
        
        self.env.StartTime()
        
        n = len(self.initial_state)
        
        init_table = table.table(self.initial_state, n)
        init_score = init_table.Manhattan(self.goal_state)
        
        self.AStarQueue.queue.put((init_score, init_table))
        c = 0
        
        while self.AStarQueue.queue:
            print(c)
            
            min_score = self.AStarQueue.queue.get()
            state = min_score[1]
            
            self.env.search_deep = len(state.path_history)
            self.env.UpdateDeep()
            
            self.explored.set.add(state)
            
            if self.goal_test(state):
                self.env.path = state.path_history
                self.env.StopTime()
                return self.env
            
            self.ExpandNode(state)
            c+=1
            
        print("Error")
        
    def ExpandNode(self, table):
            
        action = ['u', 'd', 'l', 'r']
            
        for act in action:
                
            temp_table = table.table(table.state)
                
            temp_table.path_hisroty = copy.copy(table.path_history)
                
            if temp_table.move(node):
                temp_table.path_history.append(node)
                    
                if temp_table not in self.froniter and temp_table not in self.visited:
                    temp_table.score = temp_table.manhattan(self.goal_state)
                    self.AStarQueue.queue.put((temp_table.score, temp_table))
                        
                self.env.UpdateQueue()
                    
            self.env.node_expanded +=1
            
    def GoalTest(self, state):
        if state.state == self.goal_state:
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
    
    
                
                