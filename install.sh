#!/bin/bash

echo "🔧 نصب Hiva Panel..."

sudo apt update
sudo apt install -y python3 python3-pip postgresql redis git nginx

echo "✅ نصب پیش‌نیازها انجام شد."

git clone https://github.com/0MuStAnG0/Hiva-Panel.git hivapanel
cd hivapanel

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --noinput

echo "✅ راه‌اندازی اولیه انجام شد."
