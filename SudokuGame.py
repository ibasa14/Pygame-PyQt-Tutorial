from PyQt5.QtWidgets import  QMainWindow
from PyQt5 import uic
import os
from Sudoku import load_sudoku, select_sudoku, possible, auto_resolve
import numpy as np
import time

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
		self.resolver_button.clicked.connect(self.resolve_SudokuGame)


	def resolve_SudokuGame(self):
		print('estoy en la funcion resolve_sudokuGame')
		solucion = auto_resolve(self.original_grid)

		while True:
			try:
				aux = next(solucion)
				if aux.sum() == 405:
					break
			except:
				pass

		print(aux)


		print('esta es la solucion del problema')
		print(solucion)
		#self.set_values(solucion)


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
		background_grey = {'background-color': 'grey'}

		# fila 0
		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
			self.cell00.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
			self.cell01.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
			self.cell02.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
			self.cell03.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
			self.cell04.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
			self.cell05.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
			self.cell06.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
			self.cell07.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)
			self.cell08.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")									

		# fila 1
		if self.cell10.value() != 0:
			self.cell10.setProperty('readOnly', True)
			self.cell10.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell11.value() != 0:
			self.cell11.setProperty('readOnly', True)
			self.cell11.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell12.value() != 0:
			self.cell12.setProperty('readOnly', True)
			self.cell12.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell13.value() != 0:
			self.cell13.setProperty('readOnly', True)
			self.cell13.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell14.value() != 0:
			self.cell14.setProperty('readOnly', True)
			self.cell14.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell15.value() != 0:
			self.cell15.setProperty('readOnly', True)
			self.cell15.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell16.value() != 0:
			self.cell16.setProperty('readOnly', True)
			self.cell16.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell17.value() != 0:
			self.cell17.setProperty('readOnly', True)
			self.cell17.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell18.value() != 0:
			self.cell18.setProperty('readOnly', True)	
			self.cell18.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")


		# fila 2
		if self.cell20.value() != 0:
			self.cell20.setProperty('readOnly', True)
			self.cell20.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell21.value() != 0:
			self.cell21.setProperty('readOnly', True)
			self.cell21.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell22.value() != 0:
			self.cell22.setProperty('readOnly', True)
			self.cell22.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell23.value() != 0:
			self.cell23.setProperty('readOnly', True)
			self.cell23.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell24.value() != 0:
			self.cell24.setProperty('readOnly', True)
			self.cell24.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell25.value() != 0:
			self.cell25.setProperty('readOnly', True)
			self.cell25.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell26.value() != 0:
			self.cell26.setProperty('readOnly', True)
			self.cell26.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell27.value() != 0:
			self.cell27.setProperty('readOnly', True)
			self.cell27.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell28.value() != 0:
			self.cell28.setProperty('readOnly', True)	
			self.cell28.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")


		# fila 3
		if self.cell30.value() != 0:
			self.cell30.setProperty('readOnly', True)
			self.cell30.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell31.value() != 0:
			self.cell31.setProperty('readOnly', True)
			self.cell31.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell32.value() != 0:
			self.cell32.setProperty('readOnly', True)
			self.cell32.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell33.value() != 0:
			self.cell33.setProperty('readOnly', True)
			self.cell33.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell34.value() != 0:
			self.cell34.setProperty('readOnly', True)
			self.cell34.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell35.value() != 0:
			self.cell35.setProperty('readOnly', True)
			self.cell35.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell36.value() != 0:
			self.cell36.setProperty('readOnly', True)
			self.cell36.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell37.value() != 0:
			self.cell37.setProperty('readOnly', True)
			self.cell37.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell38.value() != 0:
			self.cell38.setProperty('readOnly', True)	
			self.cell38.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")

		# fila 4
		if self.cell40.value() != 0:
			self.cell40.setProperty('readOnly', True)
			self.cell40.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell41.value() != 0:
			self.cell41.setProperty('readOnly', True)
			self.cell41.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell42.value() != 0:
			self.cell42.setProperty('readOnly', True)
			self.cell42.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell43.value() != 0:
			self.cell43.setProperty('readOnly', True)
			self.cell43.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell44.value() != 0:
			self.cell44.setProperty('readOnly', True)
			self.cell44.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell45.value() != 0:
			self.cell45.setProperty('readOnly', True)
			self.cell45.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell46.value() != 0:
			self.cell46.setProperty('readOnly', True)
			self.cell46.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell47.value() != 0:
			self.cell47.setProperty('readOnly', True)
			self.cell47.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell48.value() != 0:
			self.cell48.setProperty('readOnly', True)	
			self.cell48.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")

		# fila 5
		if self.cell50.value() != 0:
			self.cell50.setProperty('readOnly', True)
			self.cell50.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell51.value() != 0:
			self.cell51.setProperty('readOnly', True)
			self.cell51.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell52.value() != 0:
			self.cell52.setProperty('readOnly', True)
			self.cell52.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell53.value() != 0:
			self.cell53.setProperty('readOnly', True)
			self.cell53.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell54.value() != 0:
			self.cell54.setProperty('readOnly', True)
			self.cell54.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell55.value() != 0:
			self.cell55.setProperty('readOnly', True)
			self.cell55.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell56.value() != 0:
			self.cell56.setProperty('readOnly', True)
			self.cell56.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell57.value() != 0:
			self.cell57.setProperty('readOnly', True)
			self.cell57.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell58.value() != 0:
			self.cell58.setProperty('readOnly', True)	
			self.cell58.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")

		# fila 6
		if self.cell60.value() != 0:
			self.cell60.setProperty('readOnly', True)
			self.cell60.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell61.value() != 0:
			self.cell61.setProperty('readOnly', True)
			self.cell61.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell62.value() != 0:
			self.cell62.setProperty('readOnly', True)
			self.cell62.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell63.value() != 0:
			self.cell63.setProperty('readOnly', True)
			self.cell63.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell64.value() != 0:
			self.cell64.setProperty('readOnly', True)
			self.cell64.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell65.value() != 0:
			self.cell65.setProperty('readOnly', True)
			self.cell65.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell66.value() != 0:
			self.cell66.setProperty('readOnly', True)
			self.cell66.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell67.value() != 0:
			self.cell67.setProperty('readOnly', True)
			self.cell67.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell68.value() != 0:
			self.cell68.setProperty('readOnly', True)	
			self.cell68.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")

		# fila 7
		if self.cell70.value() != 0:
			self.cell70.setProperty('readOnly', True)
			self.cell70.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell71.value() != 0:
			self.cell71.setProperty('readOnly', True)
			self.cell71.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell72.value() != 0:
			self.cell72.setProperty('readOnly', True)
			self.cell72.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell73.value() != 0:
			self.cell73.setProperty('readOnly', True)
			self.cell73.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell74.value() != 0:
			self.cell74.setProperty('readOnly', True)
			self.cell74.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell75.value() != 0:
			self.cell75.setProperty('readOnly', True)
			self.cell75.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell76.value() != 0:
			self.cell76.setProperty('readOnly', True)
			self.cell76.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell77.value() != 0:
			self.cell77.setProperty('readOnly', True)
			self.cell77.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell78.value() != 0:
			self.cell78.setProperty('readOnly', True)
			self.cell78.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")

		# fila 8
		if self.cell80.value() != 0:
			self.cell80.setProperty('readOnly', True)
			self.cell80.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell81.value() != 0:
			self.cell81.setProperty('readOnly', True)
			self.cell81.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell82.value() != 0:
			self.cell82.setProperty('readOnly', True)
			self.cell82.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell83.value() != 0:
			self.cell83.setProperty('readOnly', True)
			self.cell83.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell84.value() != 0:
			self.cell84.setProperty('readOnly', True)
			self.cell84.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell85.value() != 0:
			self.cell85.setProperty('readOnly', True)
			self.cell85.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell86.value() != 0:
			self.cell86.setProperty('readOnly', True)
			self.cell86.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell87.value() != 0:
			self.cell87.setProperty('readOnly', True)
			self.cell87.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")
		if self.cell88.value() != 0:
			self.cell88.setProperty('readOnly', True)						
			self.cell88.setStyleSheet("QSpinBox {background-color: #CECACA; font-size: 20px}")