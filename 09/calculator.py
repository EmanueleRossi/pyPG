#!/usr/bin/env python
# -*- coding: utf-8 -*-
largest = None
smallest = None
while True:
    snum = input("Enter a number: ")
    if snum == "done" : 
        break
    try :
        inum = int(snum)
    except:
        print('Invalid input')
        continue
    if largest is None or inum > largest :
        largest = inum
    elif smallest is None or inum < smallest :
        smallest = inum

print("Maximum is", largest)
print("Minimum is", smallest)