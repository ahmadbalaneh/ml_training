# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:52:21 2020

@author: Ahmad - Mahsa
"""
#Calculate n!"

n=int(input("Please Enter A Number"))
c=1
for i in range(1,n):
    c=c*(i+1)
print("n!=",c)
    