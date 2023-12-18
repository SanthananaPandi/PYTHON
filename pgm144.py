# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:12:05 2023
Find out the second biggest number
@author: santh
"""
a = []
i = 0
n = int(input("Enter the value of n: "))
while i <= n-1:
    d = int(input("Enter the value of d: "))
    a.append(d)
    i = i + 1

b = 0
m = len(a)
j = 0
while j <= m-1:
    if a[j] > b:
        b = a[j]
    j = j + 1

c = 0
m = len(a)
k = 0
while k <= m-1:
    if a[k] != b:
        if a[k] > c:
            c = a[k]
    k = k + 1  

print(c)
