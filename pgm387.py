# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:52:01 2024
Find the common words in a both file.(plagarisim)
@author: santh
"""

f=open("mytext.txt")
x=f.read()
l=x.split()
a=set(l)

f=open("story.txt")
y=f.read()
k=y.split()
b=set(k)

f=open("stopwords.txt")
z=f.read()
m=z.split()
c=set(m)

d=a-c
e=b-c
file=set(d)
file_1=set(e)
common=file.intersection(file_1)
print(common)