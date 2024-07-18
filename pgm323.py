# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:04:29 2024
Pass the record of the employee to the function and print it
@author: santh
"""

def emp(**x):
    for i in x:
        print(i,x[i])
        
#main
emp(emp_id=121,emp_name='Ram',Field='IT',Salary=45000,Working_expereince=4,Branch='Chennai')