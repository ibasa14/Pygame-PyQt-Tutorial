from PyQt5.QtWidgets import  QMainWindow, QDialog
from PyQt5 import uic, QtTest
import os
from super_basastation.games.Sudoku import load_sudoku, select_sudoku, possible, auto_resolve
import numpy as np
import time


class SudokuGame(QMainWindow):
	def __init__(self, parent=None):
		super(SudokuGame, self).__init__(parent)
		uic.loadUi(os.path.join(os.environ.get('UI_PATH'), 'sudoku.ui'), self)

		self.diccionario_celdas = {
			'cell00': self.cell00,
			'cell01': self.cell01,
			'cell02': self.cell02,
			'cell03': self.cell03,
			'cell04': self.cell04,
			'cell05': self.cell05,
			'cell06': self.cell06,
			'cell07': self.cell07,
			'cell08': self.cell08,
			'cell10': self.cell10,
			'cell11': self.cell11,
			'cell12': self.cell12,
			'cell13': self.cell13,
			'cell14': self.cell14,
			'cell15': self.cell15,
			'cell16': self.cell16,
			'cell17': self.cell17,
			'cell18': self.cell18,
			'cell20': self.cell20,
			'cell21': self.cell21,
			'cell22': self.cell22,
			'cell23': self.cell23,
			'cell24': self.cell24,
			'cell25': self.cell25,
			'cell26': self.cell26,
			'cell27': self.cell27,
			'cell28': self.cell28,
			'cell30': self.cell30,
			'cell31': self.cell31,
			'cell32': self.cell32,
			'cell33': self.cell33,
			'cell34': self.cell34,
			'cell35': self.cell35,
			'cell36': self.cell36,
			'cell37': self.cell37,
			'cell38': self.cell38,
			'cell40': self.cell40,
			'cell41': self.cell41,
			'cell42': self.cell42,
			'cell43': self.cell43,
			'cell44': self.cell44,
			'cell45': self.cell45,
			'cell46': self.cell46,
			'cell47': self.cell47,
			'cell48': self.cell48,
			'cell50': self.cell50,
			'cell51': self.cell51,
			'cell52': self.cell52,
			'cell53': self.cell53,
			'cell54': self.cell54,
			'cell55': self.cell55,
			'cell56': self.cell56,
			'cell57': self.cell57,
			'cell58': self.cell58,
			'cell60': self.cell60,
			'cell61': self.cell61,
			'cell62': self.cell62,
			'cell63': self.cell63,
			'cell64': self.cell64,
			'cell65': self.cell65,
			'cell66': self.cell66,
			'cell67': self.cell67,
			'cell68': self.cell68,
			'cell70': self.cell70,
			'cell71': self.cell71,
			'cell72': self.cell72,
			'cell73': self.cell73,
			'cell74': self.cell74,
			'cell75': self.cell75,
			'cell76': self.cell76,
			'cell77': self.cell77,
			'cell78': self.cell78,
			'cell80': self.cell80,
			'cell81': self.cell81,
			'cell82': self.cell82,
			'cell83': self.cell83,
			'cell84': self.cell84,
			'cell85': self.cell85,
			'cell86': self.cell86,
			'cell87': self.cell87,
			'cell88': self.cell88,
		}

		# al construir el objeto le damos valor a sus celdas cargando uno
		# de los sudokus de forma aleatoria
		self.original_grid, self.solution = load_sudoku(select_sudoku())
		self.grid = self.original_grid.copy()
		self.set_values(self.original_grid)
		self.lock_values(self.original_grid)

		# eventos de botones
		self.resolver_button.clicked.connect(self.resolve_SudokuGame)
		self.reiniciar_button.clicked.connect(self.reset_SudokuGame)
		self.nuevo_button.clicked.connect(self.new_SudokuGame)
		self.comprobar_button.clicked.connect(self.check_SudokuGame)

		# evento al cambiar el valor de una celda
		for key, value in self.diccionario_celdas.items():
			self.diccionario_celdas[key].valueChanged.connect(self.actualize_SudokuGame)




	def resolve_SudokuGame(self):
		self.set_values(self.solution)

	def reset_SudokuGame(self):
		self.set_values(self.original_grid)

	def new_SudokuGame(self):
		self.original_grid, self.solution = load_sudoku(select_sudoku())
		self.set_values(self.original_grid)
		self.lock_values(self.original_grid)

	def check_SudokuGame(self):

		self.actualize_SudokuGame()
		for row in range(0,9):
			for col in range(0,9):
				if (possible(row, col, self.grid[row][col], self.grid)) or (self.diccionario_celdas[f"cell{row}{col}"].isReadOnly()):
					pass
				else:
					self.warning_cell(row, col)
					return 
		
		self.show_dialog_success()
		return
		

	def actualize_SudokuGame(self):
		grid_actual = self.get_values()
		self.grid = grid_actual


	def get_values(self):
		grid_auxiliar = np.zeros((9,9))
		for key, _ in self.diccionario_celdas.items():
			row = int(key[-2])
			col = int(key[-1])
			grid_auxiliar[row][col] = self.diccionario_celdas[key].value()

		return grid_auxiliar


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

		if self.cell00.value() != 0:
			self.cell00.setProperty('readOnly', True)
			self.cell00.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell00.setProperty('readOnly', False)
			self.cell00.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell01.value() != 0:
			self.cell01.setProperty('readOnly', True)
			self.cell01.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell01.setProperty('readOnly', False)
			self.cell01.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell02.value() != 0:
			self.cell02.setProperty('readOnly', True)
			self.cell02.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell02.setProperty('readOnly', False)
			self.cell02.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell03.value() != 0:
			self.cell03.setProperty('readOnly', True)
			self.cell03.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell03.setProperty('readOnly', False)
			self.cell03.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell04.value() != 0:
			self.cell04.setProperty('readOnly', True)
			self.cell04.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell04.setProperty('readOnly', False)
			self.cell04.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')
			
		if self.cell05.value() != 0:
			self.cell05.setProperty('readOnly', True)
			self.cell05.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell05.setProperty('readOnly', False)
			self.cell05.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell06.value() != 0:
			self.cell06.setProperty('readOnly', True)
			self.cell06.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell06.setProperty('readOnly', False)
			self.cell06.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell07.value() != 0:
			self.cell07.setProperty('readOnly', True)
			self.cell07.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell07.setProperty('readOnly', False)
			self.cell07.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell08.value() != 0:
			self.cell08.setProperty('readOnly', True)
			self.cell08.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell08.setProperty('readOnly', False)
			self.cell08.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell10.value() != 0:
			self.cell10.setProperty('readOnly', True)
			self.cell10.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell10.setProperty('readOnly', False)
			self.cell10.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell11.value() != 0:
			self.cell11.setProperty('readOnly', True)
			self.cell11.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell11.setProperty('readOnly', False)
			self.cell11.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell12.value() != 0:
			self.cell12.setProperty('readOnly', True)
			self.cell12.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell12.setProperty('readOnly', False)
			self.cell12.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell13.value() != 0:
			self.cell13.setProperty('readOnly', True)
			self.cell13.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell13.setProperty('readOnly', False)
			self.cell13.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell14.value() != 0:
			self.cell14.setProperty('readOnly', True)
			self.cell14.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell14.setProperty('readOnly', False)
			self.cell14.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell15.value() != 0:
			self.cell15.setProperty('readOnly', True)
			self.cell15.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell15.setProperty('readOnly', False)
			self.cell15.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell16.value() != 0:
			self.cell16.setProperty('readOnly', True)
			self.cell16.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell16.setProperty('readOnly', False)
			self.cell16.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell17.value() != 0:
			self.cell17.setProperty('readOnly', True)
			self.cell17.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell17.setProperty('readOnly', False)
			self.cell17.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell18.value() != 0:
			self.cell18.setProperty('readOnly', True)
			self.cell18.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell18.setProperty('readOnly', False)
			self.cell18.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell20.value() != 0:
			self.cell20.setProperty('readOnly', True)
			self.cell20.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell20.setProperty('readOnly', False)
			self.cell20.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell21.value() != 0:
			self.cell21.setProperty('readOnly', True)
			self.cell21.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell21.setProperty('readOnly', False)
			self.cell21.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell22.value() != 0:
			self.cell22.setProperty('readOnly', True)
			self.cell22.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell22.setProperty('readOnly', False)
			self.cell22.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell23.value() != 0:
			self.cell23.setProperty('readOnly', True)
			self.cell23.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell23.setProperty('readOnly', False)
			self.cell23.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell24.value() != 0:
			self.cell24.setProperty('readOnly', True)
			self.cell24.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell24.setProperty('readOnly', False)
			self.cell24.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell25.value() != 0:
			self.cell25.setProperty('readOnly', True)
			self.cell25.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell25.setProperty('readOnly', False)
			self.cell25.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell26.value() != 0:
			self.cell26.setProperty('readOnly', True)
			self.cell26.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell26.setProperty('readOnly', False)
			self.cell26.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell27.value() != 0:
			self.cell27.setProperty('readOnly', True)
			self.cell27.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell27.setProperty('readOnly', False)
			self.cell27.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell28.value() != 0:
			self.cell28.setProperty('readOnly', True)
			self.cell28.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell28.setProperty('readOnly', False)
			self.cell28.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell30.value() != 0:
			self.cell30.setProperty('readOnly', True)
			self.cell30.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell30.setProperty('readOnly', False)
			self.cell30.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell31.value() != 0:
			self.cell31.setProperty('readOnly', True)
			self.cell31.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell31.setProperty('readOnly', False)
			self.cell31.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell32.value() != 0:
			self.cell32.setProperty('readOnly', True)
			self.cell32.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell32.setProperty('readOnly', False)
			self.cell32.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell33.value() != 0:
			self.cell33.setProperty('readOnly', True)
			self.cell33.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell33.setProperty('readOnly', False)
			self.cell33.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell34.value() != 0:
			self.cell34.setProperty('readOnly', True)
			self.cell34.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell34.setProperty('readOnly', False)
			self.cell34.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell35.value() != 0:
			self.cell35.setProperty('readOnly', True)
			self.cell35.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell35.setProperty('readOnly', False)
			self.cell35.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell36.value() != 0:
			self.cell36.setProperty('readOnly', True)
			self.cell36.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell36.setProperty('readOnly', False)
			self.cell36.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell37.value() != 0:
			self.cell37.setProperty('readOnly', True)
			self.cell37.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell37.setProperty('readOnly', False)
			self.cell37.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell38.value() != 0:
			self.cell38.setProperty('readOnly', True)
			self.cell38.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell38.setProperty('readOnly', False)
			self.cell38.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell40.value() != 0:
			self.cell40.setProperty('readOnly', True)
			self.cell40.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell40.setProperty('readOnly', False)
			self.cell40.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell41.value() != 0:
			self.cell41.setProperty('readOnly', True)
			self.cell41.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell41.setProperty('readOnly', False)
			self.cell41.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell42.value() != 0:
			self.cell42.setProperty('readOnly', True)
			self.cell42.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell42.setProperty('readOnly', False)
			self.cell42.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell43.value() != 0:
			self.cell43.setProperty('readOnly', True)
			self.cell43.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell43.setProperty('readOnly', False)
			self.cell43.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell44.value() != 0:
			self.cell44.setProperty('readOnly', True)
			self.cell44.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell44.setProperty('readOnly', False)
			self.cell44.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell45.value() != 0:
			self.cell45.setProperty('readOnly', True)
			self.cell45.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell45.setProperty('readOnly', False)
			self.cell45.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell46.value() != 0:
			self.cell46.setProperty('readOnly', True)
			self.cell46.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell46.setProperty('readOnly', False)
			self.cell46.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell47.value() != 0:
			self.cell47.setProperty('readOnly', True)
			self.cell47.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell47.setProperty('readOnly', False)
			self.cell47.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell48.value() != 0:
			self.cell48.setProperty('readOnly', True)
			self.cell48.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell48.setProperty('readOnly', False)
			self.cell48.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell50.value() != 0:
			self.cell50.setProperty('readOnly', True)
			self.cell50.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell50.setProperty('readOnly', False)
			self.cell50.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell51.value() != 0:
			self.cell51.setProperty('readOnly', True)
			self.cell51.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell51.setProperty('readOnly', False)
			self.cell51.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell52.value() != 0:
			self.cell52.setProperty('readOnly', True)
			self.cell52.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell52.setProperty('readOnly', False)
			self.cell52.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell53.value() != 0:
			self.cell53.setProperty('readOnly', True)
			self.cell53.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell53.setProperty('readOnly', False)
			self.cell53.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell54.value() != 0:
			self.cell54.setProperty('readOnly', True)
			self.cell54.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell54.setProperty('readOnly', False)
			self.cell54.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell55.value() != 0:
			self.cell55.setProperty('readOnly', True)
			self.cell55.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell55.setProperty('readOnly', False)
			self.cell55.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell56.value() != 0:
			self.cell56.setProperty('readOnly', True)
			self.cell56.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell56.setProperty('readOnly', False)
			self.cell56.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell57.value() != 0:
			self.cell57.setProperty('readOnly', True)
			self.cell57.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell57.setProperty('readOnly', False)
			self.cell57.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell58.value() != 0:
			self.cell58.setProperty('readOnly', True)
			self.cell58.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell58.setProperty('readOnly', False)
			self.cell58.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell60.value() != 0:
			self.cell60.setProperty('readOnly', True)
			self.cell60.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell60.setProperty('readOnly', False)
			self.cell60.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell61.value() != 0:
			self.cell61.setProperty('readOnly', True)
			self.cell61.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell61.setProperty('readOnly', False)
			self.cell61.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell62.value() != 0:
			self.cell62.setProperty('readOnly', True)
			self.cell62.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell62.setProperty('readOnly', False)
			self.cell62.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell63.value() != 0:
			self.cell63.setProperty('readOnly', True)
			self.cell63.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell63.setProperty('readOnly', False)
			self.cell63.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell64.value() != 0:
			self.cell64.setProperty('readOnly', True)
			self.cell64.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell64.setProperty('readOnly', False)
			self.cell64.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell65.value() != 0:
			self.cell65.setProperty('readOnly', True)
			self.cell65.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell65.setProperty('readOnly', False)
			self.cell65.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell66.value() != 0:
			self.cell66.setProperty('readOnly', True)
			self.cell66.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell66.setProperty('readOnly', False)
			self.cell66.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell67.value() != 0:
			self.cell67.setProperty('readOnly', True)
			self.cell67.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell67.setProperty('readOnly', False)
			self.cell67.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell68.value() != 0:
			self.cell68.setProperty('readOnly', True)
			self.cell68.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell68.setProperty('readOnly', False)
			self.cell68.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell70.value() != 0:
			self.cell70.setProperty('readOnly', True)
			self.cell70.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell70.setProperty('readOnly', False)
			self.cell70.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell71.value() != 0:
			self.cell71.setProperty('readOnly', True)
			self.cell71.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell71.setProperty('readOnly', False)
			self.cell71.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell72.value() != 0:
			self.cell72.setProperty('readOnly', True)
			self.cell72.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell72.setProperty('readOnly', False)
			self.cell72.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell73.value() != 0:
			self.cell73.setProperty('readOnly', True)
			self.cell73.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell73.setProperty('readOnly', False)
			self.cell73.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell74.value() != 0:
			self.cell74.setProperty('readOnly', True)
			self.cell74.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell74.setProperty('readOnly', False)
			self.cell74.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell75.value() != 0:
			self.cell75.setProperty('readOnly', True)
			self.cell75.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell75.setProperty('readOnly', False)
			self.cell75.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell76.value() != 0:
			self.cell76.setProperty('readOnly', True)
			self.cell76.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell76.setProperty('readOnly', False)
			self.cell76.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell77.value() != 0:
			self.cell77.setProperty('readOnly', True)
			self.cell77.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell77.setProperty('readOnly', False)
			self.cell77.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell78.value() != 0:
			self.cell78.setProperty('readOnly', True)
			self.cell78.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell78.setProperty('readOnly', False)
			self.cell78.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell80.value() != 0:
			self.cell80.setProperty('readOnly', True)
			self.cell80.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell80.setProperty('readOnly', False)
			self.cell80.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell81.value() != 0:
			self.cell81.setProperty('readOnly', True)
			self.cell81.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell81.setProperty('readOnly', False)
			self.cell81.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell82.value() != 0:
			self.cell82.setProperty('readOnly', True)
			self.cell82.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell82.setProperty('readOnly', False)
			self.cell82.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell83.value() != 0:
			self.cell83.setProperty('readOnly', True)
			self.cell83.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell83.setProperty('readOnly', False)
			self.cell83.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell84.value() != 0:
			self.cell84.setProperty('readOnly', True)
			self.cell84.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell84.setProperty('readOnly', False)
			self.cell84.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell85.value() != 0:
			self.cell85.setProperty('readOnly', True)
			self.cell85.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell85.setProperty('readOnly', False)
			self.cell85.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell86.value() != 0:
			self.cell86.setProperty('readOnly', True)
			self.cell86.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell86.setProperty('readOnly', False)
			self.cell86.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell87.value() != 0:
			self.cell87.setProperty('readOnly', True)
			self.cell87.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell87.setProperty('readOnly', False)
			self.cell87.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

		if self.cell88.value() != 0:
			self.cell88.setProperty('readOnly', True)
			self.cell88.setStyleSheet('QSpinBox {background-color: #CECACA; font-size: 20px}')
		else:
			self.cell88.setProperty('readOnly', False)
			self.cell88.setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')

	def warning_cell(self, row, col):
		for _ in range(0,2):
			self.diccionario_celdas[f"cell{row}{col}"].setStyleSheet('QSpinBox {background-color: rgba(250, 10, 10, 0.8); font-size: 20px}')
			QtTest.QTest.qWait(100)
			self.diccionario_celdas[f"cell{row}{col}"].setStyleSheet('QSpinBox {background-color: white; font-size: 20px}')
			QtTest.QTest.qWait(100)

	def show_dialog_success(self):
		dialog = CustomDialog()
		dialog.exec_()

class CustomDialog(QDialog):

	def __init__(self, *args, **kwargs):
		super(CustomDialog, self).__init__(*args, **kwargs)
		uic.loadUi(os.path.join(os.environ.get('UI_PATH'), 'dialog_success.ui'), self)

		self.pushButton.clicked.connect(self.accept)
