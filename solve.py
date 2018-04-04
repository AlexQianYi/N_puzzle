#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:02:22 2018

@author: yiqian
"""

import utility
import copy


class solve:
    
    def __init__(self, input_table):
        
        self.initial_state = copy.deepcopy(self,list_to_table(input_table))       
        self.goal_state = self.set_goal_state(input_table)      
        self.AStarQueue = utility.PriorityQueue()
        
    def 
        AStartSearch(self):
            