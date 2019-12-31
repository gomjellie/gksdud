
all:
	. ./venv/bin/activate; pip install .;

test:
	python3 ./tests/test_cli.py
	python3 ./tests/test_python.py

