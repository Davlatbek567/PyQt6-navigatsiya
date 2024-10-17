import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    label = QLabel()


app = QApplication(sys.argv)
wimdow = MainWindow()
wimdow.show()
sys.exit(app.exec())