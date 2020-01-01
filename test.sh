#!/bin/bash

PYTHON3=$(which python3)

if [[ $PYTHON3 != *"venv/bin/python3" ]]; then
  echo "activate venv first!"
fi

python -m unittest discover ./tests
