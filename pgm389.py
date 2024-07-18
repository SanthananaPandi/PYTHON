# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:12:13 2024
Display the plagarisim in a table.
@author: santh
"""

m=input("Enter the original file : ")
f=open(m)
x=f.read()
y=x.split()
main=set(y)

f1=open('stopwords.txt')
a=f1.read()
b=a.split()
stop=set(b)

n=int(input("Enter the value of n : "))
files=[]
for i in range(n):
    file=input("Enter the file name : ")
    files.append(file)

diff=main.difference(stop)
length=len(diff)
print("orginal file name : ",m,",""total no of words :",length)
print("_" *125)
print("SI NO", "   |", "File Name", "    |", "No of Total Words", "  |", "No of Unique Words", "  |", "No of Duplicate Words", "  |", "Percentage of Unique Words")
print("_" *125)
x=0
for i in files:
    f2=open(i)
    q=f2.read()
    w=q.split()
    e=set(w)
    d1=main.difference(e)
    d2=e.difference(main)
    total_words_in_file=len(w)
    inter=diff.intersection(d1)
    total_unique_words=len(d2)
    percentage = (total_unique_words / total_words_in_file) * 100 
    dup=diff.intersection(d1)
    x=x+1
    print(x,'\t\t','|',i,'\t','|',len(d1),'\t\t\t\t  ','|',(len(d1)-len(inter)),'\t\t\t\t ','|',len(dup),'\t\t\t\t   ','|',percentage)
print("_" * 125)
