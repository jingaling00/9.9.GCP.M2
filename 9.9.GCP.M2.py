# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:14:01 2022

@author: jingy
"""
import math
x = float(input('Enter x: '))
n = int(input('Enter n: '))

cos_approx = 0
for n in range(n+1):
    fact = math.factorial(2*n)
    cos_approx += (((-1)**n)*(x**(2*n))/fact)

print(f'cos(x) = {cos_approx}')
actual = math.cos(x)
perc_error = math.fabs(((actual-cos_approx)/actual)*100)
print(f'Percent error = {perc_error:.2f}%')

n = int(input('Enter number of trials greater than one million: '))
import random

n_circle = 0
i = 0
while i <= n:
    x = random.random()
    y = random.random()
    dist = math.sqrt(x**2 + y**2)
    if dist <= 1:
        n_circle +=1
    i+=1

pi_est = 4*n_circle/n
print(pi_est)

    