# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:07:15 2024
Sum of the two matrix
@author: santh
"""


import random as rd
matrix=lambda n :[[rd.randint(-100,100)for i in range(n)]for j in range(n)]
n=int(input("Enter the value of n : "))
matrix_1=matrix(n)
matrix_2=matrix(n)
sum=lambda n :[[matrix_1[i][j] + matrix_2[i][j] for i in range(n)]for j in range(n)]
final=sum(n)
print(matrix_1)
print(matrix_2)
print(final)

