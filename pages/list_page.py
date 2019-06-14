import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from widgets.QBankCard import QBankCard
from widgets.QBtnLabel import QBtnLabel

# 每页显示银行卡数量
PAGE_COUNT = 2


class ListPage(QDialog):
    def __init__(self, main_app, card_list: list):
        super(ListPage, self).__init__()
        self.main_app = main_app
        self.current_page = 1
        self.card_list = card_list
        self.pages = []

        # 定义一下控件
        self.btn_previous = QPushButton('上一页', self)
        self.btn_next = QPushButton('下一页', self)
        self.btn_previous.clicked.connect(self.previous_page)
        self.btn_next.clicked.connect(self.next_page)
        self.lbl_page = QLabel('{} / {}'.format(self.current_page, len(self.pages)))
        self.lbl_page.setFont(QFont('Microsoft YaHei UI', pointSize=14, weight=10, italic=False))
        self.card1 = QBankCard('', '6217003130007648922', self)
        self.card2 = QBankCard('', '6217003130007648922', self)

        # 初始化页面 每 PAGE_COUNT 个分为一组
        self.pages = [card_list[i:i + PAGE_COUNT] for i in range(0, len(card_list), PAGE_COUNT)]

        self.initUI()

    def initUI(self):
        self._buildBackground()
        self._buildLayout()
        self._buildReturnButton()
        self.refresh_status()

        self.resize(360, 640)
        self.setFixedSize(360, 640)
        self.center()
        self.setWindowTitle('银行卡识别系统：我的卡包')
        self.setWindowIcon(QIcon('icons/main.png'))

    def _buildBackground(self):
        pix_map = QPixmap('images/bg/list.png')
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

    def _buildLayout(self):
        layout = QVBoxLayout()
        widget = QWidget(self)
        widget.resize(360, 640 - 70)
        widget.move(0, 70)
        widget.setLayout(layout)
        layout.addWidget(self.card1)
        layout.addWidget(self.card2)
        layout.addStretch(1)
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.btn_previous)
        h_layout.addStretch(1)
        h_layout.addWidget(self.lbl_page)
        h_layout.addStretch(1)
        h_layout.addWidget(self.btn_next)
        layout.addLayout(h_layout)

    def refresh_status(self):
        if self.current_page == 1:
            self.btn_previous.setEnabled(False)
        else:
            self.btn_previous.setEnabled(True)
        if self.current_page == len(self.pages):
            self.btn_next.setEnabled(False)
        else:
            self.btn_next.setEnabled(True)
        self.lbl_page.setText('{} / {}'.format(self.current_page, len(self.pages)))
        page = self.pages[self.current_page - 1]
        self.card1.setCardFile(page[0]['card_file'])
        self.card1.setCardNumber(page[0]['card_num'])
        if len(page) > 1:
            self.card2.setCardFile(page[1]['card_file'])
            self.card2.setCardNumber(page[1]['card_num'])
        else:
            self.card2.setCardFile('')
            self.card2.setCardNumber('')

    def previous_page(self):
        self.current_page -= 1
        self.refresh_status()
        # 刷新界面
        QApplication.processEvents()

    def next_page(self):
        self.current_page += 1
        self.refresh_status()
        # 刷新界面
        QApplication.processEvents()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def returnMain(self):
        self.hide()
        self.main_app.show()
