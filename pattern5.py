# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:00:41 2023

@author: milag
"""

row = int(input('ingrese un numero de fila: '))
n = 2 * row - 2  
for i in range(row, -1, -1):  
    for j in range(n, 0, -1):  
        print(end=' ')  
    n += 1  
    for j in range(0, i + 1):  
        print('* ', end='')  
    print('')  