#!/usr/bin/env bash
pip3 install virtualenv --user
python -m virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt
python -m ipykernel install --user --name=venv