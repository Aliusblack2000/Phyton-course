# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:04:55 2024

@author: alius
"""

def main():
    num=int(input("Enter number:"))
    print("Number     Square     Cube")
    print("%-4d %10d %10d"%(num,num**2,num**3))
    num += 1
    print("%-4d %10d %10d"%(num,num**2,num**3))
    num += 1
    print("%-4d %10d %10d"%(num,num**2,num**3))
    num += 1
    print("%-4d %10d %10d"%(num,num**2,num**3))
    num += 1
    print("%-4d %10d %10d"%(num,num**2,num**3))
main()