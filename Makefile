install:
	cp -fr ./pixmaps/ /usr/local/share/
	cp tkg_proxy.py /usr/local/bin/tkg_proxy
	chmod uog+x /usr/local/bin/tkg_proxy
	chmod uog+r /usr/local/share/pixmaps/tkg_proxy/*.png

	@echo
	@echo "# sudo apt-get install python3-qtpy"
	@echo "# cp tkg_proxy.desktop  ~/.config/autostart/"

uninstall:
	rm -fr /usr/local/share/pixmaps/tkg_proxy
	rm /usr/local/bin/tkg_proxy
	@echo
	@echo "# rm ~/.config/autostart/tkg_proxy.desktop"

