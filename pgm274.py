# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:15:58 2024
Construct a dictionary of ten students biodata and store into a dictionary
@author: santh
"""

for i in range(3) :
    Name = input("Enter the name :")
    Age = int(input("Enter the Age : "))
    Gender = input("Enter the Gender : ")
    Phone = int(input("Enter the phone :"))
    d={"Name" : Name ,"Age" : Age , "Gender" : Gender , "Phone" : Phone}
print(d)
