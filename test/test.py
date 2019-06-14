import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QMainWindow, QDesktopWidget, QAction, qApp
from PyQt5.QtGui import QIcon, QFont


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 14))

        self.setToolTip('This is a <b>QWidget</b> widget')
        self.statusBar().showMessage('Ready')

        btn_close = QPushButton('Click to close', self)
        btn_close.clicked.connect(QCoreApplication.instance().quit)
        btn_close.setFont(QFont('SansSerif', 14))
        btn_close.setToolTip('This is a <b>QPushButton</b> widget')
        btn_close.resize(btn_close.sizeHint())
        btn_close.move(50, 50)

        # 定义菜单栏action
        exit_action \
            = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)
        # 设置菜单栏
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)
        # 设置工具栏
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_action)

        self.resize(300, 600)
        self.center()
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
