#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:02:22 2018

@author: yiqian
"""

import utility
import copy
import environment


class solve:
    
    def __init__(self, input_table):
        
        self.initial_state = copy.deepcopy(self,list_to_table(input_table))       
        self.goal_state = self.set_goal_state(input_table)      
        self.AStarQueue = utility.PriorityQueue()
        
        self.env = environment.environment(self.AStarQueue)
        
    def AStartSearch(self):
        
        self.env.StartTime()
        
        init_table = table.table(self.initial_state)
        init_score = initial_table.manhattan_score(self.goal_state)
        
        self.AStarQueue.queue,put((init_score, init_table))
        
        while self.AStarQueue.queue:
            
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