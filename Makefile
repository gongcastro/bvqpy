build: setup.py
	python3 setup.py sdist bdist_wheel

install: build
	python3 -m pip install -e .

import:
	python3 -c 'import bvqpy'

test:
	pytest

check: install test
	python3 setup.py check

upload: check
	twine upload dist/* --skip-existing

