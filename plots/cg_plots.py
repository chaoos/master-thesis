#!/usr/bin/env python3

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

import sys
sys.path.append('../../../python/libs/')
import latex as lt

print(lt.COLORS)

A = np.array([[3, 2],
              [2, 6]])
b = np.array([2, -8])
c = 0

def f(x):
    return 0.5*x.dot(A.dot(x)) - b.dot(x) + c

def F(X, Y):
    Z = np.zeros((len(X), len(X[0])))
    for i in range(len(X)):
        for j in range(len(X[i])):
            Z[i][j] = f(np.array([X[i][j], Y[i][j]]))
    return Z

analytic_zero = np.array([2.0, -2.0])        
minimum = f(analytic_zero)
levels = [-9.9, -9, -7, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
delta = 0.1
x = np.arange(-4.0, 6.1, delta)
y = np.arange(-6.0, 4.1, delta)
X, Y = np.meshgrid(x, y)

Z = F(X, Y)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, levels=levels, cmap='coolwarm')
ax.clabel(CS, inline=1, fmt='%1.0f', fontsize=10)
ax.grid(c='k', ls='-', alpha=0.3)
plt.plot(analytic_zero[0], analytic_zero[1], '.', color=[0, 0, 1]) 
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.savefig("qform_contour.pdf")
plt.show()
