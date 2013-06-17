.PHONY: all
all:
	$(info tell me something more specific)

.PHONY: clean_old
clean_old:
	rm -rf `find . -name "*.pyc"` `find . -name "*.o"` `find . -name "*.exe"`
	rm -rf build dist deb_dist

.PHONY: clean
clean:
	git clean -xdf

.PHONY: sdist
sdist:
	./setup.py sdist

.PHONY: build
build:
	./setup.py build

.PHONY: deb2
deb2:
	$(error dont use this)
	rm -f ../pdmt-* ../pdmt_*
	git clean -xdf
	python setup.py sdist --dist-dir=../ --prune
#	python setup.py sdist --dist-dir=../
	dpkg-buildpackage -i -I -rfakeroot

.PHONY: deb
deb:
	rm -f ../pdmt-* ../pdmt_*
	git clean -xdf
	git-buildpackage

.PHONY: install-deb
install-deb:
	sudo dpkg --install deb_dist/pdmt_1-1_all.deb

.PHONY: listfiles
listfiles:
	dpkg --listfiles pdmt
.PHONY: purge
purge:
	sudo dpkg --purge pdmt
.PHONY: contents
contents:
	dpkg --contents ../pdmt_1_all.deb