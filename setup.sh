# setup
python -m venv .venv
source .venv/bin/activate
pip install django-ninja
django-admin startproject ninja_tutorial

# api test
curl "http://127.0.0.1:8000/api/add?a=1&b=2"
