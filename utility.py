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
        
    def find(self, item):
        for element in self.queue:
            if item.state == element.state:
                return True
        
        return False
    
class Frontier:
    def __init__(self):
        self.queue = deque()
        
    def find(self, item):
        for element in self.queue:
            if item.state ==element.state:
                return True
        
        return False
    
class Explored:
    def __init__(self):
        self.set = set()
        
    def find(self, item):
        for element in self.set:
            if item.state == element.state:
                return True
        return False