# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:17:58 2023

@author: milag
"""

word = str(input('ingrese una palabra: '))

n = 0

for i in word:
    n += 1
    print(word[0:n])
    
for i in word:
    n -= 1
    print(word[0:n])
    