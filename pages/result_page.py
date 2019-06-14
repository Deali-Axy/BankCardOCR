import sys

from PIL import Image
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qtpy import QtCore

from widgets.QBtnLabel import QBtnLabel

import uuid


class ResultPage(QDialog):
    def __init__(self, main_app, file_name: str, card_num: str):
        """
        :param main_app:
        :param file_name: 银行卡图片文件名
        :param card_num: 银行卡号
        """
        super().__init__()

        self.main_app = main_app
        self.file_name = file_name
        self.card_num = card_num
        self.initUI()

    def initUI(self):
        self._buildBackground()
        self._buildReturnButton()
        self._buildCard()
        self._buildNumber()

        self.resize(360, 640)
        self.setFixedSize(360, 640)
        self.center()
        self.setWindowTitle('银行卡识别系统：识别结果')
        self.setWindowIcon(QIcon('icons/main.png'))

    def _buildBackground(self):
        pix_map = QPixmap("images/bg/result.png")
        pix_map = pix_map.scaledToWidth(360)
        lbl = QBtnLabel(self)
        lbl.setPixmap(pix_map)
        lbl.resize(360, 640)

    def _buildReturnButton(self):
        pix_map = QPixmap("images/btn_return.png")
        pix_map = pix_map.scaledToWidth(22)
        lbl = QBtnLabel(self)
        lbl.setPixmap(pix_map)
        lbl.resize(44, 24)
        lbl.move(320, 30)
        lbl.raise_()
        lbl.clicked.connect(self.returnMain)

    def _buildCard(self):
        # pix_map = QPixmap("images/card.png")
        img = Image.open(self.file_name)
        card_file = f'images/temp/{uuid.uuid4().hex}@{self.card_num}.png'
        img.save(card_file)
        pix_map = QPixmap(card_file)
        pix_map = pix_map.scaledToWidth(300)
        lbl = QBtnLabel(self)
        lbl.setPixmap(pix_map)
        lbl.resize(300, 174)
        lbl.move(30, 233 - 30)
        lbl.raise_()

    def _buildNumber(self):
        lbl = QLabel('{}'.format(self.card_num), self)
        lbl.resize(360, 100)
        lbl.setAlignment(QtCore.Qt.AlignHCenter)
        lbl.setFont(QFont('Microsoft YaHei UI', pointSize=14, weight=2, italic=False))
        lbl.move(0, 233 + 174)
        lbl.raise_()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def returnMain(self):
        self.main_app.show()
        self.hide()
