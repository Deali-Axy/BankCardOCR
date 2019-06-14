import sys, os

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qtpy import QtGui

from pages.list_page import ListPage
from pages.result_page import *
from widgets.QBtnLabel import QBtnLabel


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn_start: QBtnLabel = QBtnLabel(self)
        self.btn_list: QBtnLabel = QBtnLabel(self)
        self.initUI()

    def initUI(self):
        self._buildBackground()
        self._buildStartButton()
        self._buildListButton()

        QtGui.QFontDatabase.addApplicationFont('ms.ttf')

        self.resize(360, 640)
        self.setFixedSize(360, 640)
        self.center()
        self.setWindowTitle('银行卡识别系统')
        self.setWindowIcon(QIcon('icons/main.png'))

    def _buildBackground(self):
        pix_map = QPixmap('images/bg/main.png')
        pix_map = pix_map.scaledToWidth(360)
        lbl = QLabel(self)
        lbl.setPixmap(pix_map)
        lbl.resize(360, 640)

    def _buildStartButton(self):
        pix_map = QPixmap('images/btn_start.png')
        pix_map = pix_map.scaledToWidth(240)
        lbl = self.btn_start
        lbl.setPixmap(pix_map)
        lbl.resize(240, 240)
        lbl.move(60, 74 + 147)
        # 设置在顶层，不然会被背景遮住
        lbl.raise_()

    def _buildListButton(self):
        pix_map = QPixmap('images/btn_list.png')
        pix_map = pix_map.scaledToWidth(48)
        lbl = self.btn_list
        lbl.setPixmap(pix_map)
        lbl.resize(48, 37)
        lbl.move(180 - 24, 74 + 147 + 240 + 136 - 37)
        # 设置在顶层，不然会被背景遮住
        lbl.raise_()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出确认', "确认退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def startRecognition(self):
        file_name = self.openFile()
        # QMessageBox.about(self, '打开银行卡', '文件名：{}'.format(file_name))
        self.hide()
        ResultPage(self, file_name, '卡号').exec_()

    def openDir(self):
        dir_name = QFileDialog.getExistingDirectory(self, '选择银行卡目录', '/home')
        for file_name in os.listdir(dir_name):
            # 列出文件夹中的每一个项目
            print(file_name)
        return dir_name

    def openFile(self):
        file_name = QFileDialog.getOpenFileName(self, '选择银行卡图片', '/home')
        if file_name[0]:
            return file_name[0]

    def showList(self):
        self.hide()
        cur_path = os.path.abspath(os.curdir)
        temp_path = os.path.abspath(os.path.join(cur_path, 'images', 'temp'))
        card_list = []
        for raw_name in os.listdir(temp_path):
            file_name = raw_name[0:raw_name.index('.')]
            card_file = os.path.join(temp_path, raw_name)
            card_id = file_name.split('@')[0]
            card_num = file_name.split('@')[1]
            card_create_time = os.path.getctime(card_file)
            card_list.append({
                'card_file': card_file,
                'card_id': card_id,
                'card_num': card_num,
                'card_create_time': card_create_time
            })
        card_list.sort(key=lambda item: item['card_create_time'], reverse=True)
        ListPage(self, card_list).exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.btn_start.clicked.connect(main_app.startRecognition)
    main_app.btn_list.clicked.connect(main_app.showList)
    main_app.show()
    sys.exit(app.exec_())
