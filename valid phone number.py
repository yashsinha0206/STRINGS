# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:55:53 2020

@author: 91852
"""
import sys
print("enter no.")
n=str(input())
if len(n)!=10:
    print('invalid')
    sys.exit(0)
if n[0] == '0':
    print('invalid')
    sys.exit(0)
for chr in n:
    if chr.isalpha():
        print('invalid')
        break
else:
    print('valid')