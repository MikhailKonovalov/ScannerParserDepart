import sys

from PyQt5.QtWidgets import QApplication

from src.MainWindow import MainWindow
from src.LoginWindow import LoginWindow


app = QApplication(sys.argv)


if __name__ == "__main__":
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
