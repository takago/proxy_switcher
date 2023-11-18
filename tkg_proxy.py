#! /usr/bin/python3

# GNOME系のデスクトップ(gnome/mate/cinnamon)のタスクトレイでプロキシを変更できるようにするプログラム
# 鷹合研(2023,11/17)
#

from gi.repository import Gio, GLib
from qtpy.QtGui import *
from qtpy.QtCore import *
from qtpy.QtWidgets import *
import sys


img_path='/usr/local/share/pixmaps/tkg_proxy/'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.settings = Gio.Settings(schema='org.gnome.system.proxy')

        self.my_icons = {'auto':   img_path+'auto.png',
                         'manual': img_path+'manual.png',
                         'none':   img_path+'none.png'}

        # 現在のプロキシ設定(manual/auto/none)を取得
        mode_str = self.settings.get_value('mode').unpack()
        # print(mode_str)

        # コンテキストメニューの作成
        mymenu = QMenu(self)
        group = QActionGroup(mymenu)
        self.action=dict()
        for text in list(self.my_icons.keys()):
            self.action[text] = QAction(text, mymenu, checkable=True)
            mymenu.addAction(self.action[text])
            group.addAction(self.action[text])
        group.setExclusive(True)              # 排他にする（一つチェックしたら，他のチェックが外れる）
        group.triggered.connect(self.onTriggered) # コンテキストメニューが押されたら


        # システムトレイの準備
        self.tray = QSystemTrayIcon(self)
        self.tray.setToolTip('システムプロキシの設定')
        self.tray.setIcon(QIcon(self.my_icons[mode_str])) # 現在のモードにあわせたアイコンをセット
        self.tray.setContextMenu(mymenu)                    # コンテクストメニューを開けるようにする
        self.tray.activated.connect(self.onActivated)       # クリックされたら
        self.tray.show()

        # タイマー
        self.timer = QTimer()
        self.timer.setSingleShot(False)  # 連続 or 1ショットか
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.onTimeout)
        self.timer.start()

    def onTriggered(self, action):
        new_mode_str = action.text()  # 押された項目を調べる
        # print(new_proxy_mode)
        self.settings.set_value('mode', GLib.Variant('s',new_mode_str))
        self.tray.setIcon(QIcon(self.my_icons[new_mode_str])) # アイコンの変更

    def onActivated(self, reason):  # 最新の情報を取得
        # print(return)
        return

    def onTimeout(self):                  # 一定時間ごとに
        mode_str = self.settings.get_value('mode').unpack() # モードをチェック
        self.tray.setIcon(QIcon(self.my_icons[mode_str]))   # アイコンの変更
        self.action[mode_str].setChecked(True)              # 選択状態にしておく

        if mode_str == 'auto':
            s=self.settings.get_value('autoconfig-url').unpack()
        elif mode_str == 'manual':
            s=''
            for ptcl in ['http','https','ftp','socks']:
                st = Gio.Settings(schema='org.gnome.system.proxy.'+ptcl)
                host = str(st.get_value('host').unpack())
                port = str(st.get_value('port').unpack())
                s += ptcl+'\t'+host+':'+port+'\n'
            s += 'ignore-hosts\t'+str(self.settings.get_value('ignore-hosts').unpack())
        else:
            s='no proxy'
        self.tray.setToolTip(s) # ツールチップの差し替え

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.hide() # メインウィンドウを表示しない（タスクトレイのみになる）
    sys.exit(app.exec_())
