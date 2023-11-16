#! /usr/bin/python3

# GNOME系のデスクトップ(gnome/mate/cinnamon)のタスクトレイでプロキシを変更できるようにするプログラム
# 鷹合研(2023,11/16)
#

from qtpy.QtGui import *
from qtpy.QtCore import *
from qtpy.QtWidgets import *
import sys
import os

img_path='/usr/local/share/pixmaps/tkg_proxy/'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.my_icons = {'manual': img_path+'manual.png',
                         'auto':   img_path+'auto.png',
                         'none':   img_path+'none.png'}

        # 現在のプロキシ設定(manual/auto/none)を取得
        p=os.popen("gsettings get org.gnome.system.proxy mode")
        proxy_mode=p.read().strip()[1:-1]
        p.close()
        # print(proxy_mode)

        # コンテキストメニューの作成
        mymenu = QMenu(self)
        group = QActionGroup(mymenu)
        for text in list(self.my_icons.keys()):
            action = QAction(text, mymenu, checkable=True, checked=text==proxy_mode)
            mymenu.addAction(action)
            group.addAction(action)
        group.setExclusive(True)              # 排他にする
        group.triggered.connect(self.onTriggered) # コンテキストメニューが押されたら

        # システムトレイの準備
        self.tray = QSystemTrayIcon(self)
        self.tray.setToolTip('システムプロキシの設定')
        self.tray.setIcon(QIcon(self.my_icons[proxy_mode])) # 現在のモードにあわせたアイコンをセット
        self.tray.setContextMenu(mymenu)                    # コンテクストメニューを開けるようにする
        self.tray.show()

    def onTriggered(self, action):
        new_proxy_mode = action.text()  # 押された項目を調べる
        # print(new_proxy_mode)
        cmd="gsettings set org.gnome.system.proxy mode '%s'" % new_proxy_mode
        os.system(cmd)
        self.tray.setIcon(QIcon(self.my_icons[new_proxy_mode])) # アイコンの変更

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.hide() # メインウィンドウを表示しない（タスクトレイのみになる）
    sys.exit(app.exec_())
