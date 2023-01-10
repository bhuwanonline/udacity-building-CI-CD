ls

git clone https://github.com/bhuwanonline/udacity-building-CI-CD.git

cd udacity-building-CI-CD

pip install virtualenv
virtualenv ~/.myrepo
source ~/.myrepo/bin/activate
python --version
deactivate


az webapp up -n udacity-flask-ml-service

az webapp log tail
