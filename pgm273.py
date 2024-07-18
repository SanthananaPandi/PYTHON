# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 18:58:31 2024
Read a Biodata from the keyboard and store into a dictionary
@author: santh
"""

Name = input("Enter the name :")
Age = int(input("Enter the Age : "))
Gender = input("Enter the Gender : ")
Phone = int(input("Enter the phone :"))

d={"Name" : Name ,"Age" : Age , "Gender" : Gender , "Phone" : Phone}
print(d)