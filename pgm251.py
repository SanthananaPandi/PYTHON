# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 17:55:58 2023
Construct a list of foreign temperature into a centigrated temperature from (0 to 100)
@author: santh
"""

a=[5/9 * (f-32) for f in range(101)]
print(a)