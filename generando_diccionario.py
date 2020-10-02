# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:05:02 2020

@author: nacho
"""

import os

PATH = r'C:\Users\nacho\Desktop\super-basastation'

filename = os.path.join(PATH, 'diccionario_celdas.txt')


diccionario = ""
for row in range (0,9):
    for col in range(0,9):
        diccionario += f"'cell{row}{col}': self.cell{row}{col},\n\t" 
        
        
        

        

with open( filename, 'w') as archivo:
    archivo.write(diccionario)