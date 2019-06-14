import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, ):
        super(QMainWindow, self).__init__()

        w = QWidget()
        self.setCentralWidget(w)

        self.topFiller = QWidget()
        # 设置控件最小尺寸
        self.topFiller.setMinimumSize(250, 2000)
        for filename in range(20):
            self.MapButton = QPushButton(self.topFiller)
            self.MapButton.setText(str(filename))
            self.MapButton.move(10, filename * 40)

        # 创建一个滚动条
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        w.setLayout(self.vbox)

        self.resize(360, 640)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
