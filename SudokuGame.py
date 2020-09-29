from PyQt5.QtWidgets import  QMainWindow
from PyQt5 import uic
import os
from Sudoku import load_sudoku, select_sudoku

UI_PATH = os.path.join(os.getcwd(), 'ui')


class SudokuGame(QMainWindow):
	def __init__(self, parent=None):
		super(SudokuGame, self).__init__(parent)
		uic.loadUi(os.path.join(UI_PATH, 'sudoku.ui'), self)

		# al construir el objeto le damos valor a sus celdas cargando uno
		# de los sudokus de forma aleatorio
		self.original_grid = load_sudoku(select_sudoku())
		self.grid = self.original_grid.copy()
		self.set_values(self.original_grid)
		self.lock_values(self.original_grid)


	def set_values(self,grid):
		self.cell00.setValue(grid[0,0])
		self.cell01.setValue(grid[0,1])
		self.cell02.setValue(grid[0,2])
		self.cell03.setValue(grid[0,3])
		self.cell04.setValue(grid[0,4])
		self.cell05.setValue(grid[0,5])
		self.cell06.setValue(grid[0,6])
		self.cell07.setValue(grid[0,7])
		self.cell08.setValue(grid[0,8])

		self.cell10.setValue(grid[1,0])
		self.cell11.setValue(grid[1,1])
		self.cell12.setValue(grid[1,2])
		self.cell13.setValue(grid[1,3])
		self.cell14.setValue(grid[1,4])
		self.cell15.setValue(grid[1,5])
		self.cell16.setValue(grid[1,6])
		self.cell17.setValue(grid[1,7])
		self.cell18.setValue(grid[1,8])

		self.cell20.setValue(grid[2,0])
		self.cell21.setValue(grid[2,1])
		self.cell22.setValue(grid[2,2])
		self.cell23.setValue(grid[2,3])
		self.cell24.setValue(grid[2,4])
		self.cell25.setValue(grid[2,5])
		self.cell26.setValue(grid[2,6])
		self.cell27.setValue(grid[2,7])
		self.cell28.setValue(grid[2,8])

		self.cell30.setValue(grid[3,0])
		self.cell31.setValue(grid[3,1])
		self.cell32.setValue(grid[3,2])
		self.cell33.setValue(grid[3,3])
		self.cell34.setValue(grid[3,4])
		self.cell35.setValue(grid[3,5])
		self.cell36.setValue(grid[3,6])
		self.cell37.setValue(grid[3,7])
		self.cell38.setValue(grid[3,8])

		self.cell40.setValue(grid[4,0])
		self.cell41.setValue(grid[4,1])
		self.cell42.setValue(grid[4,2])
		self.cell43.setValue(grid[4,3])
		self.cell44.setValue(grid[4,4])
		self.cell45.setValue(grid[4,5])
		self.cell46.setValue(grid[4,6])
		self.cell47.setValue(grid[4,7])
		self.cell48.setValue(grid[4,8])

		self.cell50.setValue(grid[5,0])
		self.cell51.setValue(grid[5,1])
		self.cell52.setValue(grid[5,2])
		self.cell53.setValue(grid[5,3])
		self.cell54.setValue(grid[5,4])
		self.cell55.setValue(grid[5,5])
		self.cell56.setValue(grid[5,6])
		self.cell57.setValue(grid[5,7])
		self.cell58.setValue(grid[5,8])

		self.cell60.setValue(grid[6,0])
		self.cell61.setValue(grid[6,1])
		self.cell62.setValue(grid[6,2])
		self.cell63.setValue(grid[6,3])
		self.cell64.setValue(grid[6,4])
		self.cell65.setValue(grid[6,5])
		self.cell66.setValue(grid[6,6])
		self.cell67.setValue(grid[6,7])
		self.cell68.setValue(grid[6,8])

		self.cell70.setValue(grid[7,0])
		self.cell71.setValue(grid[7,1])
		self.cell72.setValue(grid[7,2])
		self.cell73.setValue(grid[7,3])
		self.cell74.setValue(grid[7,4])
		self.cell75.setValue(grid[7,5])
		self.cell76.setValue(grid[7,6])
		self.cell77.setValue(grid[7,7])
		self.cell78.setValue(grid[7,8])

		self.cell80.setValue(grid[8,0])
		self.cell81.setValue(grid[8,1])
		self.cell82.setValue(grid[8,2])
		self.cell83.setValue(grid[8,3])
		self.cell84.setValue(grid[8,4])
		self.cell85.setValue(grid[8,5])
		self.cell86.setValue(grid[8,6])
		self.cell87.setValue(grid[8,7])
		self.cell88.setValue(grid[8,8])

	def lock_values(self, grid):

		# fila 0
		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)									

		# fila 1
		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)	


		# fila 2
		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)	


		# fila 3
		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)	

		# fila 4
		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)	

		# fila 5
		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)	

		# fila 6
		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)	

		# fila 7
		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)

		# fila 8
		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)						