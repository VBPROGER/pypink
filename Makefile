SHELL := /usr/bin/env bash
.SILENT: install clean

install:
	echo 'Installing...'
	pip3 install -e .
clean:
	rm -rf *.o
	rm -rf __pycache__