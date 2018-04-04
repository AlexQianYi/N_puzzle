#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:58:02 2018

@author: yiqian
"""
import sys

if __name__ == "__main__":
    # 读取第一行的n
    arr = input().strip().split(' ')
    n = int(arr[0])
    time = int(arr[-1])
    
    area = int(arr[-2])*int(arr[-2])
    area_temp = 0
    score = 0
    res = 0
    for i in range(1, n+1):
        score = (int(arr[i])*int(arr[i])-area_temp)*(n-i)+score
    res = (score/area)*time
    print(round(res, 3))
