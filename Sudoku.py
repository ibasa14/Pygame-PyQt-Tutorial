import pandas as pd
import os
import time
import random
import numpy as np
import copy
import tqdm
import joblib

SUDOKU_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sudokusdb')

def select_sudoku():
    '''
    Lee todos los archivos de la carpeta sudokusdb y devuelve uno 
    de manera aleatoria
    @return: nombre de archivo de sudoku
    '''
    choices = os.listdir(SUDOKU_FOLDER)
    choice = np.random.choice(choices)

    return choice

def load_sudoku(filename):
    '''
    Carga un sudoku y lo devuelve en formato Numpy 2D
    @param: nombre del archivo
    @return: numpy array sudoku
    '''
    grid = joblib.load(os.path.join(SUDOKU_FOLDER, filename))
    return grid
    


class Sudoku():


    def __init__(self, array2D):
        self.array=array2D
        self.cuadrants={}
        self.fixed_cells=[]
    
    def checkRow(self, row, column):
        if np.sum(self.array[row,:]==self.array[row, column])>1:
            return False
        return True
    
    def checkRowCompleted(self, row):
        if np.sum(self.array[row,:]==0) > 0:
            return False
        else:
            return True
    
    def checkColumn(self, row, column):
        if np.sum(self.array[:,column]==self.array[row, column])>1:
            return False
        return True

    def checkColumnCompleted(self, column):
        if np.sum(self.array[:,column]==0) > 0:
            return False
        else:
            return True

    def generateCuadrants(self):
        self.cuadrants[1]=self.array[0:3,0:3]
        self.cuadrants[2]=self.array[0:3,3:6]
        self.cuadrants[3]=self.array[0:3,6:9]
        self.cuadrants[4]=self.array[3:6,0:3]
        self.cuadrants[5]=self.array[3:6,3:6]
        self.cuadrants[6]=self.array[3:6,6:9]
        self.cuadrants[7]=self.array[6:9,0:3]
        self.cuadrants[8]=self.array[6:9,3:6]
        self.cuadrants[9]=self.array[6:9,6:9]

    def getCuadrant(self, row, column):
        return self.cuadrants[3*int(row/3)+int(column/3)+1]
            
    def checkCuadrant(self, cuadrant, row, column):
        aux_array=cuadrant.flatten()
        if np.sum(aux_array==self.array[row, column])>1:
            #print('El numero {}, aparece: {} veces'.format(self.array[row,column],np.sum(aux_array==self.array[row, column])))
            return False
        return True

    def checkCuadrantCompleted(self, cuadrant):
        if np.sum(cuadrant.flatten()==0) > 0:
            return False
        else:
            return True

    def copy(self):
        return copy.copy(self)        

    '''def isCorrect(self):
        for r in range(0, 9):
            for c in range(0,9):
                if not self.checkRow(r,c) or not self.checkColumn(r,c):
                    return False
        for cuadrant in self.cuadrants.values():
            if not self.checkCuadrant(cuadrant):
                return False
        return True'''

    def nextCell(self, x, y):
        if (x,y)==(8,8):
            return (-1,-1)
        if y==8:
            if (x+1,0) in self.fixed_cells:
                self.nextCell(x+1,0)
            return (x+1,0)
        else:
            if (x, y+1) in self.fixed_cells:
                self.nextCell(x, y+1)
            return (x, y+1)

    def autoResolve(self):
        tracking_dict={0:{}}
        step=0
        tracking_dict[0]['sudoku']=self.copy()
        tracking_dict[0]['cell']=(0,0)
        tracking_dict[0]['choices']=[1,2,3,4,5,6,7,8,9]
        tracking_dict[0]['sudoku'].generateCuadrants()
        fixed_cells_aux=np.where(self.array!=0)
        self.fixed_cells=list(zip(fixed_cells_aux[0], fixed_cells_aux[1]))
        imposible=False
        iteracion = 0
        while ((not tracking_dict[step]['sudoku'].checkRow(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])) or (not tracking_dict[step]['sudoku'].checkColumn(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])) or (not tracking_dict[step]['sudoku'].checkCuadrant(tracking_dict[step]['sudoku'].getCuadrant(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]), tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])) or (tracking_dict[step]['sudoku'].array[tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]]==0) or (not tracking_dict[step]['sudoku'].checkCuadrantCompleted(tracking_dict[step]['sudoku'].getCuadrant(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]))) or (not  tracking_dict[step]['sudoku'].checkRowCompleted(tracking_dict[step]['cell'][0])) or (not  tracking_dict[step]['sudoku'].checkColumnCompleted(tracking_dict[step]['cell'][1]) )):           
            #print('empezamos de nuevo el bucle')
            print(f'iteracion: {iteracion}', end = '\r')
            iteracion +=1
            try:
                num=random.choice(tracking_dict[step]['choices'])
                tracking_dict[step]['choices'].remove(num)
                tracking_dict[step]['sudoku'].array[tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]]=num
                #print ('step: {},\nsudoku:\n{},\ncell: {}\nchoices: {}'.format(step, tracking_dict[step]['sudoku'].array, tracking_dict[step]['cell'], tracking_dict[step]['choices']))
                #print('Check row: {}'.format(tracking_dict[step]['sudoku'].checkRow(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])))
                #print('Check column: {}'.format(tracking_dict[step]['sudoku'].checkColumn(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])))
                #print('Check cuadrant {}: {}'.format(tracking_dict[step]['sudoku'].getCuadrant(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]),tracking_dict[step]['sudoku'].checkCuadrant(tracking_dict[step]['sudoku'].getCuadrant(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]), tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])))
                #print('Set number: {}'.format(tracking_dict[step]['sudoku'].array[tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]]))
                #print('\n')
                if ((not tracking_dict[step]['sudoku'].checkRow(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])) or (not tracking_dict[step]['sudoku'].checkColumn(tracking_dict[step]['cell'][0], tracking_dict[step]['cell'][1])) or (not tracking_dict[step]['sudoku'].checkCuadrant(tracking_dict[step]['sudoku'].getCuadrant(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]),tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])) ):
                    continue
                step+=1
                try:
                    tracking_dict[step]
                except KeyError:
                    tracking_dict[step]={}
                    tracking_dict[step]['sudoku']=tracking_dict[step-1]['sudoku'].copy()
                    tracking_dict[step]['cell']=tracking_dict[step-1]['sudoku'].nextCell(tracking_dict[step-1]['cell'][0], tracking_dict[step-1]['cell'][1])
                    tracking_dict[step]['choices']=[1,2,3,4,5,6,7,8,9]
                    tracking_dict[step]['sudoku'].generateCuadrants()

                
            except IndexError:
                tracking_dict[step]['choices']=[1,2,3,4,5,6,7,8,9]
                tracking_dict[step]['sudoku'].array[tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]]=0
                step-=1
                #print('restamos un step')
                if tracking_dict[step]['cell']==(0,0):
                    #print('no se puede resolver')
                    imposible=True
                    break
                continue
        if imposible:
            return (np.zeros((9,9)))
        else:
            #print('si alguna de las siguientes condiciones es False, entonces deberia haberse ejecutado el while')
            #print('checkrow: {}'.format(tracking_dict[step]['sudoku'].checkRow(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])))
            #print('checkcol: {}'.format(tracking_dict[step]['sudoku'].checkColumn(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])))
            #print('checkcuadrant {}'.format(tracking_dict[step]['sudoku'].checkCuadrant(tracking_dict[step]['sudoku'].getCuadrant(tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]), tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1])))
            #print('is cero: {}'.format(tracking_dict[step]['sudoku'].array[tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]]==0))
            print('The solution to this sudoku problem is: \n')
            print(tracking_dict[step]['sudoku'].array)
            return (tracking_dict[step]['sudoku'].array)


            














        
            





    