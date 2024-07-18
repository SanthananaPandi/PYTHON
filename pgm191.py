# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:22:17 2023
Print only the vowels of the given string
@author: santh
"""
a='Linsoft Academy'
n=len(a)
for i in range(0,n):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        print(a[i])