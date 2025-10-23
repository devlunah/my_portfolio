#!/bin/bash

# Instala as dependências
pip install -r requirements.txt

# Coleta os arquivos estáticos
python3 manage.py collectstatic --noinput