pip3 install virtualenv
virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt
#pip3 install -r faiss.txt
python -m ipykernel install --user --name=venv
