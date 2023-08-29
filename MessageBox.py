from PyQt5.QtWidgets import QMessageBox


class MessageBox(QMessageBox):
    def __init__(self, icon, title, text, buttons=QMessageBox.Ok, callback=None, parent=None):
        super().__init__(icon, title, text, buttons, parent)

        if callback is not None:
            self.buttonClicked.connect(callback)


# class Dialog(QDialog):
#     def __init__(self, title, text, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.setWindowTitle(title)

#         layout = QVBoxLayout(self)
#         label = QLabel(text, self)
#         layout.addWidget(label)


# class CustomDialog(QDialog):
#     def __init__(self, icon_type, title, text, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle(title)
#         layout = QVBoxLayout()
#         label = QLabel(text)
#         layout.addWidget(label)

#         if button_flags & Qt.WindowSystemMenuHint:
#             self.add_ok_button(callback, layout)
        
#         if button_flags & Qt.WindowTitleHint:
#             self.add_cancel_button(layout)

#         if icon_type:
#             icon_label = QLabel()
#             icon_pixmap = self.get_icon_pixmap(icon_type)
#             icon_label.setPixmap(icon_pixmap)
#             layout.addWidget(icon_label)


#         if callback is not None:
#             self.callback = callback
#             ok_button = QPushButton("OK")
#             ok_button.clicked.connect(self.handle_ok_button)
#             layout.addWidget(ok_button)

#         self.setLayout(layout)

#     def add_ok_button(self, callback, layout):
#         ok_button = QPushButton("OK")
#         ok_button.clicked.connect(callback)
#         layout.addWidget(ok_button)

#     def add_cancel_button(self, layout):
#         cancel_button = QPushButton("Cancel")
#         cancel_button.clicked.connect(self.reject)  # Закрывает диалог без сохранения изменений
#         layout.addWidget(cancel_button)

#     def handle_ok_button(self):
#         if hasattr(self, 'callback') and callable(self.callback):
#             self.callback()
#         self.accept()

#     def get_icon_pixmap(self, icon_type):
#         message_box_icon = self.map_icon_type(icon_type)
#         pixmap = QPixmap.fromImage(message_box_icon)
#         return pixmap

#     def map_icon_type(self, icon_type):
#         return QMessageBox().standardIcon(icon_type).pixmap(QSize(64, 64)).toImage()





