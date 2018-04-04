#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 11:04:54 2018

@author: yiqian
"""

class GameTreeNode:
    
    def __init__(self, table, father, action, priority):
        self.table = table
        self.father = father
        self.action = action
        self.priority = priority
        
    def compare(self, GameTreeNode):
        if self.priority == GameTreeNode.priority:
                return self.table.manhattan() - GameTreeNode.manhattan()
            
        else:
            return self.priority - GameTreeNode.priority
        
    