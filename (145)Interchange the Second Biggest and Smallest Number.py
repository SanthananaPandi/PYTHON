# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:05:54 2023
Interchange the second biggest and smallest number
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
            z = k
    k = k + 1
d = 0
m = len(a)
l = 0
while l <= m-1:
    if a[l] < d:
        d = a[l]
    l = l + 1
e = 0
m = len(a)
q = 0
x = 0
while q <= m-1:
    if a[q] != d:
        if a[q] < e:
            e = a[q]
            x = q
    q = q + 1
a[z] = e
a[x] = c
print(a)
