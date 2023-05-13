# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:50:41 2023

@author: milag
"""

row = int(input('ingrese un numero de fila: '))  
for i in range(row + 1, 0, -1):    
    for j in range(0, i - 1):  
        print('* ', end='')  
    print(' ')
    