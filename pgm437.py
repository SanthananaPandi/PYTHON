# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:21:49 2024
Construct a person class
@author: santh
"""

class person():
    _Name=None
    _age=None
    _address=None
    _mobile=None
    
    def __init__(self,Name='Vijay',age=30,address='Trichy',mobile=98424321):
        
        self._Name=Name
        self._age=age
        self._address=address
        self._mobile=mobile
        
    def display(self):
        print(self._Name,self._age,self._address,self._mobile)
        
    def setname(self,Name):
        self._Name=Name
        
    def setage(self,age):
        self._age=age
        
    def setaddress(self,address):
        self._address=address
        
    def setmobile(self,mobile):
        self._mobile=mobile
        
    def setall(self,Name,age,address,mobile):
        self._Name=Name
        self._age=age
        self._address=address
        self._mobile=mobile
        
    def reset(self):
        self._Name='Ajay'
        self._age=32
        self._address='Madurai'
        self._mobile=9842150801
        
    def setObject(self,a):
        self._Name=a._Name
        self._age=a._age
        self._address=a._address
        self._mobile=a._mobile
        
    def getName(self):
        return self._Name
    
    def getage(self):
        return  self._age
    
    def getaddress(self):
        return self._address
    
    def getmobile(self):
        return self._mobile
    
    def getall(self):
        return self._Name,self._age,self._address,self._mobile
    
    def getObject(self):
        return self
        
    
#main

c=person()
c.display()

c.setname('Raghu')
c.display()

c.setage(10)
c.display()

c.setaddress('Karur')
c.display()

c.setmobile(9842180801)
c.display()

c.setall('Ravi',25,'Chennai',9894007453)
c.display()

c.reset()
c.display()

d=person()
c.setObject(d)

a=c.getName()
b=c.getage()
g=c.getaddress()
f=c.getmobile()
m=c.getall()


print(a)
print(b)
print(g)
print(f)
print(m)

x=c.getObject()
x.display()
    