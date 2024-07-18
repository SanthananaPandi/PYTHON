# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 10:43:21 2024
Percentage of common words in both a file.
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

file_1=set(d)
file_2=set(e)

common=file_1.intersection(file_2)
total_words=file_1.union(file_2)
length=len(total_words)
percentage=(len(common)/length)*100

print("Percentage of common words : ",percentage,"\n")
print("Common words : ",common)

