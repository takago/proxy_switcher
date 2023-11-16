# proxy_switcher
Proxy switching tool that runs in the systemtray of the GNOME/MATE/CINNAMON desktop environment

![](https://github.com/takago/proxy_switcher/blob/main/screenshot.png)

```
git clone https://github.com/takago/proxy_switcher.git
cd proxy_switcher

# インストールと自動起動の登録
sudo apt-get install python3-qtpy
sudo make install
cp tkg_proxy.desktop  ~/.config/autostart/

# アンインストール
sudo make uninstall
rm ~/.config/autostart/tkg_proxy.desktop

# ここでログインし直せばOK
```
