install:
	python3 -m pip install -e .

import:
	python3 -c 'import bvqpy'

build: setup.py
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/* --skip-existing

check:
	python3 setup.py check