def test(*args):
    for p in args:
        print(p[0])

a = 1
b = 2
c = 3
test((a,"aaa"), (b,"bbb"),(c,"ccc"))



from PySide2.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
QLabel, QLineEdit, QPushButton, QComboBox, QCheckBox, QMessageBox, 
QApplication, QGridLayout, QFormLayout,QGroupBox,QDialogButtonBox,QFileDialog,QPlainTextEdit)

from PySide2.QtGui import QIcon, QColor

RED = QColor(1,1,0)

print(RED)
