# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 19:02:09 2023
Print only vowels of the given string
@author: santh
"""
a='Linsoft Academy'
n=len(a)
i=0
while i<=n-1:
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]== 'u' :
        print(a[i])
    else:
        pass
    i=i+1

