#!/bin/bash

PYTHON3=$(which python3)

if [[ $PYTHON3 != *"venv/bin/python3" ]]; then
  echo "activate venv first!"
fi

python3 ./tests/test_cli.py
python3 ./tests/test_python.py
