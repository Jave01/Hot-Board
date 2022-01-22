from msilib.schema import SelfReg
import random
import os
import sys
from PySide6.QtGui import QPalette, QColor, QKeyEvent
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QPushButton,
    QApplication, 
    QVBoxLayout, 
    QHBoxLayout, 
    QGridLayout,
    QComboBox,
    QLineEdit,
    QButtonGroup,
    QStackedLayout
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
        self.keylist = []

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
        self.cmb.setPlaceholderText("Select a switch")
        self.cmb.addItems(["Hotkey", "Execute File", "Open URL", "Disabled"])
        self.cmb.currentTextChanged.connect(self.combo_box_text_changed)
        self.cmb.setEnabled(False)
        l1.addWidget(self.cmb)

        self.arg_input = QLineEdit()
        self.arg_input.setPlaceholderText("Arguments")
        self.arg_input.setFixedSize(QSize(WIDTH//3, 25))
        self.arg_input.textEdited.connect(self.macro_argument_text_changed)
        self.arg_input.setEnabled(False)
        l1.addWidget(self.arg_input)
        apply_button = QPushButton("Apply")
        apply_button.clicked.connect(self.applied)
        l1.addWidget(apply_button)

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
        
        if self.active_button.macro_action == "":
            self.cmb.setCurrentIndex(-1)
        else:
            self.cmb.setCurrentText(self.active_button.macro_action)

    def applied(self):
        self.arg_input.setText("")

    def combo_box_text_changed(self):
        self.active_button.macro_action = self.cmb.currentText()
        self.arg_input.setText("")

        if self.active_button.macro_action == "" or self.active_button.macro_action == "Disabled":
            self.arg_input.setEnabled(False)
        else:
            self.arg_input.setEnabled(True)


    def macro_argument_text_changed(self):
        if self.cmb.currentText().lower() == "hotkey":
            if not self.arg_input.text()[-1].isalpha():
                self.arg_input.setText(self.arg_input.text()[:-1])


    def keyPressEvent(self, event: QKeyEvent):
        self.firstRelease = True
        print(event.text())
        self.keylist.append(str(event.key()))


    def keyReleaseEvent(self, event: QKeyEvent):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()