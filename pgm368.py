# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 17:28:32 2024

@author: santh
"""

def menu():
    print("1.Copy all the chatracters from the string")
    print("2.Extract n characters")
    print("3.Copy from mth position")
    print("4.Copy the last n characters ")
    print("5.Copy n characters from the right side")
    print("6.Reverse the given string")
    print("7.Given string is palindrome or not")
    print("8.Given integer is palindrome or not")
    print("9.Reverse using negative indexing")
    print("10.Copy n character from mth position using negative indexing")
    print("11.Copy last n character from the right edge")
    print("12.copy n character from the mth position")
    n=int(input("Enter the value of n : "))
    return n

def copy_all(s):
    b=s[0:]
    return b

def Extract_n(s,m):
    b=s[0:m]
    return b

def copy_mp(s,m):
    b=s[m:]
    return b

def copy_last_n(s,m):
    n=len(s)
    a=n-m
    b=s[a:]
    return b

def n_char_right(s,n):
    b=s[-1:-n:-1]
    return b

def Reverse(s):
    b=s[::-1]
    return b

def s_palindrome(s):
    b=s[::-1]
    if s==b:
        print("palindrome")
    else:
        print("Not a palindrome")

def i_palindrome(a):
    s=str(a)
    b=s[::-1]
    c=int(b)
    if a==c:
        print("Palindrome")
    else:
        print("Not")
        
def Rev_negative(s):
    b=s[-1::-1]
    return b

def copy_n_m_negative(s,n,m):
    x=m+n
    b=s[-m:-x:-1]
    return b

def copy_last_n_Right(s,m):
    n=len(s)
    a=m-n
    b=s[-a::-1]
    return b

def copy_n_m(s,n,m):
    x=m+n
    b=s[m:x]
    return b

#main
x=menu()
s=input("Enter the value of s : ")
while x!=13:
    if x==1:
        y=copy_all(s)
        print(y)
    elif x==2:
        m=int(input("Enter the value of m : "))
        y=Extract_n(s,m)
        print(y)
    elif x==3:
        m=int(input("Enter the value of m : "))
        y=copy_mp(s,m)
        print(y)
    elif x==4:
        m=int(input("Enter the value of m : "))
        y=copy_last_n(s,m)
        print(y)
    elif x==5:
        n=int(input("Enter the value of n : "))
        y=n_char_right(s,n)
        print(y)
    elif x==6:
        y=Reverse(s)
        print(y)
    elif x==7:
        y=s_palindrome(s)
        print(y)
    elif x==8:
        a=int(input("Enter the value of a : "))
        y=i_palindrome(a)
        print(y)
    elif x==9:
        y=Rev_negative(s)
        print(y)
    elif x==10:
        n=int(input("Enter the value of n : "))
        m=int(input("Enter the value of m : "))
        y=copy_n_m_negative(s,n,m)
        print(y)
    elif x==11:
        m=int(input("Enter the value of m : "))
        y=copy_last_n_Right(s,m)
        print(y)
    elif x==12:
        n=int(input("Enter the value of n : "))
        m=int(input("Enter the value of m : "))
        y=copy_n_m(s,n,m)
        print(y)
    else:
        pass
    x=menu()
        
        