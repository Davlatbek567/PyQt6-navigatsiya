import sys

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QWidget, QLabel, QPushButton, QStackedWidget
from PyQt6.QtCore import Qt

class Pages(QWidget):
    def __init__(self,  content: str):
        super().__init__()
        label = QLabel(content)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        
        self.setLayout(layout)
        
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        
        self.page1 = Pages("Salom Davlatbek")
        self.page2 = Pages("Salom Azizbek")
        
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        
        button_1 = QPushButton("  ")
        button_1.setMaximumWidth(100)
        button_1.clicked.connect(lambda : self.stacked_widget.setCurrentWidget(self.page1))
        
        button_2 = QPushButton("  ")
        button_2.setMaximumWidth(100)
        button_2.clicked.connect(lambda : self.stacked_widget.setCurrentWidget(self.page2))
        
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button_1)
        layout.addWidget(button_2)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(self.stacked_widget)
        
        self.setLayout(main_layout)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())