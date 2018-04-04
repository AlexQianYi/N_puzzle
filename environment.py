#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:08:25 2018

@author: yiqian
"""

import copy
import time

class environment:
    
    def __init__(self, queue):
        self.path = []
        self.node_expanded = 0
        self.queue = queue
        self.max_queue = 0
        self.search_deep = 0
        self.max_deep = 0
        self.start_time = 0
        self.end_time = 0
        self.search_time = 0
    
    # return how many steps do we need 
    def PathCost(self):
        return len(self.path)
    
    # return length of queque
    def LengthQueue(self):
        return len(self.queue.queue)
    
    def UpdateQueue(self):
        queue_length = self.UpdateQueue()
        if queue_length > self.max_queue:
            self.max_queue = queue_length
            
    def UpdateDeep(self):
        if self.search_deep > self.max_deep:
            self.max_deep = copy.copy(self.search_deep)
            
    def StartTime(self):
        self.start_time = time.time()
        
    def StopTime(self):
        self.end_time = time.time()
        self.search_time = "{0:.2f}".format((self.end_time - self.start_time) * 1000)
        
    