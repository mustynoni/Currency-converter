import sys

from PyQt5.QtWidgets import QApplication
from currency_converter import MainWindow

app = QApplication(sys.argv)
MainWindow().show()
sys.exit(app.exec_())