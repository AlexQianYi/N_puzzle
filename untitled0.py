#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:52:09 2018

@author: yiqian
"""

import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = map(int, line.split())
    time = int(sys.stdin.readline().strip())

    res = 0
    score = 0
    area = 0
    for i in range(n):
        score = (n-i)*(values[i]**2)+score
        area = (values[i]**2)+area
    res = score/area
    print(res)