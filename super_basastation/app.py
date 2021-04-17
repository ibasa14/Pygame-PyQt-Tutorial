from PyQt5.QtWidgets import  QApplication, QWidget, QMainWindow, QStackedWidget
from PyQt5 import uic
import sys
import os
from super_basastation.games import resources
from super_basastation.games.SudokuGame import SudokuGame
#from threading import Thread


os.chdir(os.path.dirname(os.path.abspath(__file__)))
UI_PATH = os.path.join(os.getcwd(), 'ui')
SUDOKU_FOLDER = os.path.join(os.getcwd(), 'games','sudokusdb', 'problemas')
SOLUTION_FOLDER = os.path.join(os.getcwd(), 'games', 'sudokusdb', 'soluciones')

os.environ['UI_PATH'] = UI_PATH
os.environ['SUDOKU_FOLDER'] = SUDOKU_FOLDER
os.environ['SOLUTION_FOLDER'] = SOLUTION_FOLDER
os.environ['SNAKE_ON'] = 'False'
os.environ['PONG_ON'] = 'False'



class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setStyleSheet("background-color: rgb(0,0,0);") 
		self.resize(890, 660)
		self.stackedWidget = QStackedWidget()
		self.setCentralWidget(self.stackedWidget)

		### Intro
		self.intro = Intro()
		self.stackedWidget.addWidget(self.intro)
		self.intro.pushButton.clicked.connect(self.go_to_seleccion_juego)

		### Seleccion juego
		self.seleccion_juego = SeleccionJuego()
		self.seleccion_juego.sudoku_label.mousePressEvent = self.open_sudoku
		self.seleccion_juego.snake_label.mousePressEvent = self.open_snake
		self.seleccion_juego.brick_label.mousePressEvent = self.open_pong


		self.stackedWidget.addWidget(self.seleccion_juego)

		### Sudoku game
		self.sudoku_game = SudokuGame()

	def go_to_seleccion_juego(self):
		self.stackedWidget.setCurrentIndex(1)

	def open_sudoku(self, event):
		self.sudoku_game.show()

	def open_snake(self, event):
		os.system('python games/SnakeGame.py')

	def open_pong(self, event):
		os.system('python games/SelfPongGame.py')

class Intro(QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		uic.loadUi(os.path.join(UI_PATH, 'intro.ui'), self)

class SeleccionJuego(QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		uic.loadUi(os.path.join(UI_PATH, 'seleccion_juego.ui'), self)




def run():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())