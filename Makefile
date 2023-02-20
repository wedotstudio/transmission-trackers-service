AUTOMAKE_OPTIONS = foreign
DESTDIR ?=
PREFIX ?= /usr

PREFIX_NAME = transmission-trackers-service


all: install

install: service_install
	install -Dm 755 $(PREFIX_NAME).py $(DESTDIR)$(PREFIX)/share/transmission-trackers-service

uninstall: service_uninstall
	rm -f $(DESTDIR)$(PREFIX)/share/$(PREFIX_NAME)/*.sh

service_install:
	install -Dm 644 $(PREFIX_NAME).service $(DESTDIR)/etc/systemd/system
	install -Dm 644 $(PREFIX_NAME).timer $(DESTDIR)/etc/systemd/system

service_uninstall: disable_service
	rm -f $(DESTDIR)/etc/systemd/system/$(PREFIX_NAME).service
	rm -f $(DESTDIR)/etc/systemd/system/$(PREFIX_NAME).timer

enable_service:
	systemctl daemon-reload
	systemctl enable $(PREFIX_NAME).timer
	systemctl start $(PREFIX_NAME).timer

disable_service:
	systemctl stop $(PREFIX_NAME).timer
	systemctl disable $(PREFIX_NAME).timer

remove: uninstall