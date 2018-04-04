#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:18:18 2018

@author: yiqian
"""
import copy

class table:
    
    def __init__(self, input_table, N):
        self.table = copy.deecopy(input_table)
        
        self.step_path = []
        self.score = 0
        self.n = N