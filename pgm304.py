# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:22:06 2024
Find out the key words of the given string
@author: santh
"""

a=[]
s=input("Enter the value of s : ")
a.append(s)
l=s.split()
x=set(l)
stopwords={'is','are','they','was','if','it','at','in','a','or','to','of','and','also','by','with'}
w=x-stopwords
key=set(w)
print("Given : ",x)
print("Keywords : ",key)
