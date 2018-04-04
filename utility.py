#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 11:52:30 2018

@author: yiqian
"""

from collections import deque
import Queue

class PriorityQueue:
    
    def __init__(self):
        self.queue = Queue.PriorityQueue()
        
    def find(self, item):
        for element in self.queue:
            if item.state == element.state:
                return True
        
        return False