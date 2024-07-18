# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:12:37 2024
Extract only the keywords of the file.
@author: santh
"""

f=open("mytext.txt")
x=f.read()
l=x.split()
a=set(l)

f=open("stopwords.txt")
y=f.read()
k=y.split()
b=set(k)

c=a-b
keywords=set(c)
print(keywords)