PKGNAME=pykickstart
VERSION=$(shell awk '/Version:/ { print $$2 }' ${PKGNAME}.spec)
RELEASE=$(shell awk '/Release:/ { print $$2 }' ${PKGNAME}.spec)
CVSTAG=r$(subst .,_,$(VERSION)-$(RELEASE))

MANDIR=/usr/share/man
PREFIX=/usr

default: all

all:

clean:
	-rm *.tar.gz pykickstart/*.pyc
	python setup.py -q clean --all

install: all
	python setup.py install --root=$(DESTDIR)

tag:
	cvs tag -FR $(CVSTAG)

archive: tag
	@rm -rf /tmp/${PKGNAME}-$(VERSION) /tmp/${PKGNAME}
	@CVSROOT=`cat CVS/Root`; cd /tmp; cvs -d $$CVSROOT export -r$(CVSTAG) ${PKGNAME}
	@mv /tmp/${PKGNAME} /tmp/${PKGNAME}-$(VERSION)
	@cd /tmp/${PKGNAME}-$(VERSION) ; python setup.py -q sdist
	@cp /tmp/${PKGNAME}-$(VERSION)/dist/${PKGNAME}-$(VERSION).tar.gz .
	@rm -rf /tmp/${PKGNAME}-$(VERSION)
	@echo "The archive is in ${PKGNAME}-$(VERSION).tar.gz"

local:
	@rm -rf ${PKGNAME}-$(VERSION).tar.gz
	@rm -rf /tmp/${PKGNAME}-$(VERSION) /tmp/${PKGNAME}
	@dir=$$PWD; cp -a $$dir /tmp/${PKGNAME}-$(VERSION)
	@cd /tmp/${PKGNAME}-$(VERSION) ; python setup.py -q sdist
	@cp /tmp/${PKGNAME}-$(VERSION)/dist/${PKGNAME}-$(VERSION).tar.gz .
	@rm -rf /tmp/${PKGNAME}-$(VERSION)	
	@echo "The archive is in ${PKGNAME}-$(VERSION).tar.gz"