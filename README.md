# proxy_switcher (tkg_proxy)
Proxy switching tool that runs in the systemtray of the GNOME/MATE/CINNAMON desktop environment

Gnome系デスクトップ環境のシステムトレイ上でプロキシ設定を確認したり，切り替えたりできるツールを作ってみました．

![](https://github.com/takago/proxy_switcher/blob/main/screenshot01.png)

![](https://github.com/takago/proxy_switcher/blob/main/screenshot02.png)

アイコンは inkscape でテキトウに作りました

![](https://github.com/takago/proxy_switcher/blob/main/omake.svg)


----
## インストール
```
git clone https://github.com/takago/proxy_switcher.git
cd proxy_switcher

# インストールと自動起動の登録
sudo apt-get install python3-qtpy  python3-gi
sudo make install
cp tkg_proxy.desktop  ~/.config/autostart/

# アンインストール
sudo make uninstall
rm ~/.config/autostart/tkg_proxy.desktop

```
----
## 補足（大学のプロキシをLinuxに登録する方法）
学内サーバに接続できる環境で，以下のコマンドを一度だけ実行してください．
```
cd /tmp
wget http://darkside.info.kanazawa-it.ac.jp/~takago/set_systemproxy.sh
chmod +x set_systemproxy.sh
./set_systemproxy.sh
```
