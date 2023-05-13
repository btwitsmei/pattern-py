# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:25:13 2023

@author: milag
"""

row = int(input('ingrese un numero de fila: '))
n = 2 * row - 2
for i in range(0, row):
    for j in range(0, n):
        print(end= ' ')
    n -= 1
    for j in range(0, i + 1):
        print('* ', end= '') 
    print('')
    