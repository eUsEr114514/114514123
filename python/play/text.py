import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

class LinkApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('电子的软件')
        self.setGeometry(100, 100, 400, 300)

        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QVBoxLayout()
        widget.setLayout(layout)

        button1 = QPushButton('点击打开我的bilibili')
        button1.clicked.connect(self.openDuckDuckGo)
        layout.addWidget(button1)

        button2 = QPushButton('点击打开我的抖音')
        button2.clicked.connect(self.openGoogle)
        layout.addWidget(button2)

    def openDuckDuckGo(self):
        QDesktopServices.openUrl(QUrl('https://space.bilibili.com/553343171'))

    def openGoogle(self):
        QDesktopServices.openUrl(QUrl('https://www.douyin.com/user/MS4wLjABAAAASMvQCRAzLp1_daonfImRs1oVREuPWd6s2yqTCIvog1uGW9hr69UmAz9WRnvmcWsX'))

if __name__ == '__main__':
    print("欢迎来到我的软件！")
    app = QApplication(sys.argv)
    link_app = LinkApp()
    link_app.show()
    sys.exit(app.exec_())