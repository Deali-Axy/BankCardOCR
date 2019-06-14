from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from widgets.QBtnLabel import QBtnLabel


class QBankCard(QWidget):
    def __init__(self, card_file: str = '', card_num: str = '', parent=None):
        super(QBankCard, self).__init__(parent)
        self.card_file = card_file
        self.card_num = card_num
        # 控件
        # self.pix_map: QPixmap = QPixmap(self.card_file)
        self.pix_map: QPixmap = QPixmap("images/card.png")
        self.lbl_card: QLabel = QLabel(self)
        self.lbl_num: QLabel = QLabel(self)
        # 初始化ui
        self.initUI()

    def initUI(self):
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        # pix_map = QPixmap(self.card_file)
        self.pix_map = self.pix_map.scaledToWidth(300)
        self.lbl_card.setPixmap(self.pix_map)
        self.lbl_card.resize(300, 174)

        self.lbl_num.setText('银行卡号：{}'.format(self.card_num))
        self.lbl_num.setFont(QFont('Microsoft YaHei UI', pointSize=14, weight=2, italic=False))

        v_layout.addWidget(self.lbl_card)
        v_layout.addWidget(self.lbl_num)
        h_layout.addStretch(1)
        h_layout.addLayout(v_layout)
        h_layout.addStretch(1)

        self.setLayout(h_layout)

    def setCardFile(self, card_file: str):
        if len(card_file) == 0:
            self.lbl_card.setPixmap(QPixmap())
            return
        self.card_file = card_file
        self.pix_map = QPixmap(self.card_file)
        self.pix_map = self.pix_map.scaledToWidth(300)
        self.lbl_card.setPixmap(self.pix_map)

    def setCardNumber(self, card_num: str):
        if len(card_num) == 0:
            self.lbl_num.setText('')
            return
        self.card_num = card_num
        self.lbl_num.setText('银行卡号：{}'.format(self.card_num))
