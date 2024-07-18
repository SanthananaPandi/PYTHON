# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:10:27 2024
Difference of the two matrixes
@author: santh
"""

import random as rd
matrix=lambda n :[[rd.randint(-100,100)for i in range(n)]for j in range(n)]
n=int(input("Enter the value of n : "))
matrix_1=matrix(n)
matrix_2=matrix(n)
diff=lambda n :[[matrix_1[i][j] - matrix_2[i][j] for i in range(n)]for j in range(n)]
final=diff(n)
print(matrix_1)
print(matrix_2)
print(final)

