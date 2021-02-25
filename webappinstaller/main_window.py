from PyQt5.QtWidgets import QMainWindow

from . import ui_mainwindow


class MainWindow(QMainWindow, ui_mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
