# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:09:10 2023

@author: milag
"""

row = int(input('ingrese un numero de fila: '))

for i in range(0, row):  
    for j in range(0, i + 1):  
        print('* ', end='')
    print('')  