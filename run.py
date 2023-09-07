import sys

from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow


app = QApplication(sys.argv)


if __name__ == "__main__":
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
