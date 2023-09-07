from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox
from PyQt5.QtCore import Qt

from MessageBox import MessageBox
from handler import OperationThread


# Main class window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Program Scanner')
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel('Перетащите файл сюда', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 50, 300, 200)
        self.label.setStyleSheet('border: 2px dashed #aaa;')

        self.statusBar().showMessage('Программа ожидает файл') 

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            self.file_path = event.mimeData().urls()[0].toLocalFile()
            self.showConfirmDialog()


    def showConfirmDialog(self):
        self.msg_box = MessageBox(
            QMessageBox.Question,
            'Подтверждение отправки',
            f'Вы уверены, что хотите отправить файл:\n\n{self.file_path}',
            QMessageBox.Ok | QMessageBox.Cancel,
            self.handle_upload_data
            )
        self.msg_box.exec_()
        

    def handle_upload_data(self, result):
        if result.text() == '&OK':
            self.msg_box.hide()
            self.statusBar().showMessage('Идет обработка файла')
            self.OperationThread = OperationThread(self.file_path)
            self.OperationThread.operation_complete.connect(self.handle_operation_complete)
            self.OperationThread.start()
            
        elif result.text() == '&Cancel':
            ...


    def handle_operation_complete(self):
        if self.OperationThread.result == 'Error: Maximum retries reached':
            print(self.OperationThread.result)
            self.statusBar().showMessage('Файл не был обработан')
            return


        self.statusBar().showMessage('Файл был обработан')

        self.msg_box2 = MessageBox(
                QMessageBox.Question,
                'Подтверждение отправки',
                f'Вы уверены, что хотите отправить файл в отдел: {self.OperationThread.result}',
                QMessageBox.Ok | QMessageBox.Cancel,
                #lambda: self.handle_upload_department(self.OperationThread.result)
                lambda depart: self.handle_upload_department(depart, self.OperationThread.result)
                )
        self.msg_box2.exec_()
       
    def handle_upload_department(self, result, depart):
        data = ['Юридический', 'Бухгалтерия', 'Учебный', 'Деканат', 'Охрана']
        print(depart)
        if depart in data:
            self.statusBar().showMessage(f'Файл был отправлен в отдел: {depart}')

        else:
            self.statusBar().showMessage('Не удалось отправить файл')

    # function for executing an event when closing
    def closeEvent(self, event):
        # Временно
        # if self.OperationThread.isRunning():
        #     self.OperationThread.quit()
        #     self.OperationThread.wait()
        event.accept()

