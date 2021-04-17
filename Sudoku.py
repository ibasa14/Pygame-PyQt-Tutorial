import pandas as pd
import os
import time
import random
import numpy as np
import copy
import tqdm
import joblib

SUDOKU_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sudokusdb', 'problemas')
SOLUTION_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sudokusdb', 'soluciones')


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
    @return: tuple (numpy array sudoku problema, numpy array sudoku solucion)
    '''
    numero_sudoku = os.path.splitext(filename)[0].split('_')[1]
    problema = joblib.load(os.path.join(SUDOKU_FOLDER, filename))
    solucion = joblib.load(os.path.join(SOLUTION_FOLDER, f'solucion_{numero_sudoku}.pkl'))
    return (problema, solucion)
    
def possible(y,x,n, grid):
    #compruebo toda la fila
    for i in range(0,9):
        if grid[y][i] == n and i != x:
            return False
    for i in range(0,9):
        if grid[i][x] == n and i != y:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n and y0+i != y and x0+j != x:
                return False
    return True

			

def auto_resolve(grid):
    """
    Resuelve el sudoku original directamente y muestra la solucion.
    @param: numpy array sudoku
    """
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n,grid):
                        grid[y][x] = n
                        auto_resolve(grid)
                        grid[y][x] = 0
                return
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
            return False
        return True

    def checkCuadrantCompleted(self, cuadrant):
        if np.sum(cuadrant.flatten()==0) > 0:
            return False
        else:
            return True

    def copy(self):
        return copy.copy(self)        

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
            print(f'iteracion: {iteracion}', end = '\r')
            iteracion +=1
            try:
                num=random.choice(tracking_dict[step]['choices'])
                tracking_dict[step]['choices'].remove(num)
                tracking_dict[step]['sudoku'].array[tracking_dict[step]['cell'][0],tracking_dict[step]['cell'][1]]=num

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
                if tracking_dict[step]['cell']==(0,0):
                    imposible=True
                    break
                continue
        if imposible:
            return (np.zeros((9,9)))
        else:

            print('The solution to this sudoku problem is: \n')
            print(tracking_dict[step]['sudoku'].array)
            return (tracking_dict[step]['sudoku'].array)


            














        
            





    