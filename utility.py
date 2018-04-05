#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 11:52:30 2018

@author: yiqian
"""

from collections import deque
import queue

class PriorityQueue:
    
    def __init__(self):
        self.queue = queue.PriorityQueue()
        
    def __contains__(self, item):
        for element in self.queue:
            if item.table == element.table:
                return True
        
        return False
    
class Frontier:
    def __init__(self):
        self.queue = deque()
        
    def __contains__(self, item):
        for element in self.queue:
            if item.table ==element.table:
                return True
        
        return False
    
class Explored:
    def __init__(self):
        self.set = []
        
    def __contains__(self, item):
        for element in self.set:
            if item == element:
                return True
        return False