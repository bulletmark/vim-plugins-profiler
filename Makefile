# Copyright (C) 2016 Mark Blakeney. This program is distributed under
# the terms of the GNU General Public License.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or any
# later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License at <http://www.gnu.org/licenses/> for more
# details.

DOC = README.md

SCRIPT = vim-plugins-profiler
MODULE = vim_plugins_profiler

DOCOUT = $(DOC:.md=.html)

all:
	@echo "Type sudo make install|uninstall, or make doc|check|clean"

install:
	@python setup.py install --root=$(or $(DESTDIR),/) --optimize=1

uninstall:
	@rm -vrf /usr/bin/$(SCRIPT)* /etc/$(SCRIPT).conf \
	    /usr/share/doc/$(MODULE) \
	    /usr/lib/python*/site-packages/*$(MODULE)* \
	    /usr/lib/python*/site-packages/*/*$(MODULE)*

sdist:
	python3 setup.py sdist

upload: sdist
	twine upload dist/*

doc:	$(DOCOUT)

check:
	flake8 $(MODULE).py $(SCRIPT) setup.py

$(DOCOUT): $(DOC)
	markdown $< >$@

clean:
	@rm -vrf $(DOCOUT) *.egg-info build/ dist/ __pycache__/
