# Django Minimal Starter

Look at https://docs.djangoproject.com/en/4.1/intro/tutorial01/ to learn more.
Look at https://docs.digitalocean.com/tutorials/app-deploy-django-app/ to learn how to deploy django on Digital Ocean

mettere link host

## Local Setup

Make sure to have django (>=4.1.5) and Python (>= 3.9.12) installed:

```bash
# 0] Upgrade pip if necessary
python -m pip install --upgrade pip

# 1] Install the requirements
pip install -r requirements.txt

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
## Environment Variables
Inside /mysite/mysite you need to create a .env file containing the following informations

SECRET_KEY=your_backend_secret_key
```bash
DATABASE_NAME=db.sqlite3
DATABASE_URL=sqlite
DEVELOPMENT_MODE=True
```


## Development Server

Start the development server on http://127.0.0.1:8000

```bash
python manage.py runserver
```
