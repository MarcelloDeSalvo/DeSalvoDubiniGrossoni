# Django Minimal Starter

Look at https://docs.djangoproject.com/en/4.1/intro/tutorial01/ to learn more.

mettere link host

## Local Setup

Make sure to have django (>=4.1.5) and Python (>= 3.9.12) installed:

```bash
# 1] Upgrade pip if necessary
python -m pip install --upgrade pip

# 2] clone the repo and switch to the Back-end branch
git clone https://github.com/MarcelloDeSalvo/DeSalvoDubiniGrossoni

# 3] create a virtual environment 
python -m venv django

# 4] activate the environment
django\Scripts\activate.bat

# 5] install Django
python -m pip install Django 

# 6] run the server
python manage.py runserver

# 7] test it
http://127.0.0.1:8000

```

## Development Server

Start the development server on http://127.0.0.1:8000

```bash
python manage.py runserver
```
