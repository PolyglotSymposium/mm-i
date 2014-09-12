#!/bin/sh
py3=python3
if [[ $(python --version) == Python\ 3* ]]; then
    py3=python
fi
$py3 -m unittest *_specs.py
