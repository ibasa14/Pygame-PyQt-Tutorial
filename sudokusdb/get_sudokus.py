# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import pandas as pd
import numpy as np
import os
import joblib

PATH = r'C:\Users\Nacho\super-basastation\sudokusdb'

PATH_PROBLEMAS = os.path.join(PATH, 'problemas')

PATH_SOLUCIONES = os.path.join(PATH, 'soluciones')

if os.path.isdir(PATH_PROBLEMAS):
       pass
else:
       os.mkdir(PATH_PROBLEMAS)
       
if os.path.isdir(PATH_SOLUCIONES):
       pass
else:
       os.mkdir(PATH_SOLUCIONES)
       
       
def char_to_int(char):
       return(int(char))
       
def string_to_np(string):
       aux_list = [c for c in string]
       array = np.array(list(map(char_to_int, aux_list)))
       return array.reshape(9,9)
       


sudokus = pd.read_csv(os.path.join(PATH, 'sudoku.csv'))


sudokus_100 = sudokus.loc[:100]

for row in sudokus_100.iterrows():
       problema = string_to_np(row[1][0])
       solucion = string_to_np(row[1][1])
       
       joblib.dump(problema, os.path.join(PATH_PROBLEMAS, f'problema_{row[0]}.pkl'))
       joblib.dump(solucion, os.path.join(PATH_SOLUCIONES, f'solucion_{row[0]}.pkl'))
       
       print(f'row: {row[0]}', end = '\r')
