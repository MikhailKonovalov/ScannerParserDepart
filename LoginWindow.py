from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно авторизации")
        self.setFixedSize(450, 300)

        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)

        form_layout = QFormLayout()

        username_label = QLabel("Имя пользователя:")
        username_label.setFont(QFont('Arial', 12))
        username_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText('Введите имя пользователя')
        self.username_entry.setFont(QFont('Arial', 12))
        

        password_label = QLabel("Пароль:")
        password_label.setFont(QFont('Arial', 12))

        self.password_entry = QLineEdit()
        self.password_entry.setPlaceholderText('Введите пароль')
        self.password_entry.setFont(QFont('Arial', 12))
        self.password_entry.setEchoMode(QLineEdit.Password)

        # form_layout.addRow(username_label, self.username_entry)
        # form_layout.addRow(password_label, self.password_entry)

        login_button = QPushButton("Войти")
        login_button.setStyleSheet('''
            background-color: #008CBA;
            border: none;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        ''')
        login_button.clicked.connect(self.login)

        layout.addWidget(username_label, alignment=Qt.AlignLeft)
        layout.addWidget(self.username_entry)
        layout.addWidget(password_label, alignment=Qt.AlignLeft)
        layout.addWidget(self.password_entry)
        layout.addWidget(login_button, alignment=Qt.AlignCenter)

        layout.addLayout(form_layout)
        layout.addWidget(login_button, alignment=Qt.AlignCenter)

        self.apply_style(self.username_entry)
        self.apply_style(self.password_entry)

    def apply_style(self, widget):
        widget.setStyleSheet('''
            background-color: #FFFFFF;
            border: 2px solid #D3D3D3;
            border-radius: 5px;
            font-size: 16px;
            padding: 5px;
        ''')

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        if username == "admin" and password == "password":
            print("Успешная авторизация!")
        else:
            print("Неправильное имя пользователя или пароль.")
