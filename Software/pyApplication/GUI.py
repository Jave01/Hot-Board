from msilib.schema import SelfReg
import random
import os
import sys
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication, QPalette, QColor
from PySide6.QtCore import QSize, Qt, QRect
from PySide6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QPushButton, 
    QTabWidget, 
    QApplication, 
    QVBoxLayout, 
    QHBoxLayout, 
    QGridLayout,
    QComboBox,
    QLineEdit,
    QButtonGroup
)
WIDTH = 800
HEIGHT = 500

class Color(QWidget):
    """ Dummy class for creating colored planes """
    def __init__(self, *args):
        super(Color, self).__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()

        palette.setColor(QPalette.Window, QColor(*args))

        self.setPalette(palette)

        self.width=200


class PushButton(QPushButton):
    def __init__(self):
        super(PushButton, self).__init__()

        self.macro_action = ""
        self.macro_action_args = ""


class  MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Hot-Board")
        self.setFixedSize(QSize(WIDTH, HEIGHT))

        overall_layout = QVBoxLayout()
        buttons_layout = QGridLayout()
        settings_layout = QHBoxLayout()

        self.btn_group = QButtonGroup()
        self.active_button = None

        for i in range(3):
            for j in range(4):
                btn = PushButton()
                btn.setCheckable(True)
                btn.setFixedSize(60, 50)
                btn.clicked.connect(self.clicked)

                self.btn_group.addButton(btn, id=i)
                buttons_layout.addWidget(btn, i, j)

        buttons_layout.setContentsMargins(WIDTH//3, 0, WIDTH//3, 0)

        l1 = QVBoxLayout()
        self.cmb = QComboBox()
        self.cmb.setPlaceholderText("Select a key")
        self.cmb.addItems(["Hotkey", "Execute File", "Open URL"])
        self.cmb.currentTextChanged.connect(self.combo_box_text_changed)
        self.cmb.setEnabled(False)
        l1.addWidget(self.cmb)

        self.arg_input = QLineEdit()
        self.arg_input.setPlaceholderText("arguments")
        self.arg_input.setFixedSize(QSize(WIDTH//3, 25))
        l1.addWidget(self.arg_input)
        l1.addWidget(QPushButton("Save"))

        settings_layout.addLayout(l1)

        overall_layout.addLayout(buttons_layout)
        overall_layout.addLayout(settings_layout)

        w = Color(0x40, 0x40, 0x40)
        w.setLayout(overall_layout)

        self.setCentralWidget(w)

        


    def clicked(self):
        self.active_button = self.btn_group.checkedButton()
        self.arg_input.setText(self.active_button.macro_action_args)
        
        if not self.cmb.isEnabled():
            self.cmb.setEnabled(True)
            self.cmb.setPlaceholderText("Select an action")
        

    def combo_box_text_changed(self):
        print(self.cmb.currentText())
        self.active_button.macro_action = self.cmb.currentText().lower()


    def macro_argument_text_changed(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()