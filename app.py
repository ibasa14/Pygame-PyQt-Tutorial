from PyQt5.QtWidgets import  QApplication, QWidget, QMainWindow, QStackedWidget
from PyQt5 import uic
import sys
import os
import resources

UI_PATH = os.path.join(os.getcwd(), 'ui')

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setStyleSheet("background-color: rgb(0,0,0);") 
		self.resize(890, 660)
		self.stackedWidget = QStackedWidget()
		self.setCentralWidget(self.stackedWidget)
		self.intro = Intro()
		self.stackedWidget.addWidget(self.intro)
		self.intro.pushButton.clicked.connect(self.go_to_seleccion_juego)
		self.seleccion_juego = SeleccionJuego()
		self.stackedWidget.addWidget(self.seleccion_juego)

	def go_to_seleccion_juego(self):
		self.stackedWidget.setCurrentIndex(1)




class Intro(QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		uic.loadUi(os.path.join(UI_PATH, 'intro.ui'), self)

class SeleccionJuego(QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		uic.loadUi(os.path.join(UI_PATH, 'seleccion_juego.ui'), self)

class SudokuGame(QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		uic.loadUi(os.path.join(UI_PATH, 'seleccion_juego.ui'), self)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())