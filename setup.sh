#!/bin/bash

python3 -m venv .venv

.venv/bin/pip install -r requirements.txt

echo "Зависимости установлены."
echo "Запуск проекта..."

.venv/bin/python sandbox_test.py

chmod +x setup.sh