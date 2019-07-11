#!/usr/bin/env python
# -*- coding: utf-8 -*-
def computepay(h, r):
    if h > 40 :
        pay = 40 * r + (h - 40) * 1.5 * r
    else :
        pay = h * r
    return pay

hrs = input("Enter Hours: ")
hrf = float(hrs)
rs = input("Enter Rate: ")
rf = float(rs)

p = computepay(hrf, rf)
print("Pay: ", p)