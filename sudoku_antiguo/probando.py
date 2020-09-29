from Sudoku import Sudoku
import joblib
import os
import time
import numpy as np


array=np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])



if __name__=='__main__':
	#print(possible(array, 2, 2, 4))

	path=os.path.dirname(os.path.realpath(__file__))
	file_name='misudoku.pkl'
	f=os.path.join(path,file_name)
	sudoku=Sudoku(np.array([[5,3,0,0,7,0,0,0,0],
							[6,0,0,1,9,5,0,0,0],
							[0,9,8,0,0,0,0,6,0],
							[8,0,0,0,6,0,0,0,3],
							[4,0,0,8,0,3,0,0,1],
							[7,0,0,0,2,0,0,0,6],
							[0,6,0,0,0,0,2,8,0],
							[0,0,0,4,1,9,0,0,5],
							[0,0,0,0,8,0,0,7,9]]))

	joblib.dump(np.array([[5,3,0,0,7,0,0,0,0],
							[6,0,0,1,9,5,0,0,0],
							[0,9,8,0,0,0,0,6,0],
							[8,0,0,0,6,0,0,0,3],
							[4,0,0,8,0,3,0,0,1],
							[7,0,0,0,2,0,0,0,6],
							[0,6,0,0,0,0,2,8,0],
							[0,0,0,4,1,9,0,0,5],
							[0,0,0,0,8,0,0,7,9]]), 'sudoku.pkl')
	print(sudoku.array)
	start_time=time.time()
	sudoku.autoResolve()
	print('\n')
	print(f'Se han tardado {time.time()-start_time} segundos.')


	#grid = sudoku.array.copy()

	"""grid1 = np.array([[5,3,0,0,7,0,0,0,0],
						[6,0,0,1,9,5,0,0,0],
						[0,9,8,0,0,0,0,6,0],
						[8,0,0,0,6,0,0,0,3],
						[4,0,0,8,0,3,0,0,1],
						[7,0,0,0,2,0,0,0,6],
						[0,6,0,0,0,0,2,8,0],
						[0,0,0,4,1,9,0,0,5],
						[0,0,0,0,8,0,0,7,9]])
			
				grid = np.array([[0,0,0,0,2,0,0,6,0],
						[0,0,0,0,0,0,2,0,0],
						[0,0,0,4,0,0,1,0,5],
						[0,1,0,0,4,0,0,7,0],
						[0,6,0,0,0,1,5,0,0],
						[0,0,7,2,0,3,0,0,0],
						[0,0,0,5,0,0,3,8,0],
						[7,0,2,3,0,0,0,0,0],
						[0,9,0,0,0,2,0,5,0]])
			
				#print(grid1, type(grid1))
				print(grid, type(grid))
			
			
				def possible(y,x,n):
					global grid
					for i in range(0,9):
						if grid[y][i] == n:
							return False
					for i in range(0,9):
						if grid[i][x] == n:
							return False
					x0 = (x // 3) * 3
					y0 = (y // 3) * 3
					for i in range(0,3):
						for j in range(0,3):
							if grid[y0+i][x0+j] == n:
								return False
					return True
			
			
				iteracion = 0
				def autoResolve_recursively():
					global grid
					global iteracion
					print(f'Iteracion: {iteracion}', end = '\r')
					iteracion += 1
					for y in range(9):
						for x in range(9):
							if grid[y][x] == 0:
								for n in range(1,10):
									if possible(y,x,n):
										grid[y][x] = n
										autoResolve_recursively()
										grid[y][x] = 0
								return
			
					#print(grid)
			
				autoResolve_recursively()
				print(grid)
				#print(autoResolve_recursively())
				print('\n')
				print(f'Se han tardado {time.time()-start_time} segundos.')
			"""

