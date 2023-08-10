# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:11:13 2023
Extract a character other than vowels
@author: santh
"""
s=input("Enter the value of s: " )
n=len(s)
z=''
i=0
while i<=n-1:
    if s[i]!='a' and s[ i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u' :
        z=z+s[i] 
    else:
        pass
    i=i+1
print(z)


