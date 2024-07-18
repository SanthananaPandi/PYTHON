# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:30:38 2024
Print the line that has highest number of words.
@author: santh
"""

f=open("my.txt")
x=1
d={}
for i in f:
    length=len(i)
    words=i.split()
    len_word=len(words)
    d[x]=[length,i,words,len_word]
    x=x+1
y=0
for i in d:
    if d[i][3]>y:
        y=d[i][3]
        s=i
print(s,d[s][1])
