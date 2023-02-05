# Django Minimal Starter

Look at https://docs.djangoproject.com/en/4.1/intro/tutorial01/ to learn more.  
Look at https://docs.digitalocean.com/tutorials/app-deploy-django-app/ to learn how to deploy django on Digital Ocean

Deployed at https://sea-lion-app-4fmmp.ondigitalocean.app/cpms

## Local Setup

Make sure to have the dependencies and Python (>= 3.9.12) installed:

```bash
# Upgrade pip if necessary
python -m pip install --upgrade pip

# Optional: create a virtual environment named "django" with your favourite env. manager (in this ex. venv)
python -m venv /path/to/new/virtual/environment/django

# Optional: activate the environment
path\django\Scripts\activate.bat [WINDOWS]
source path/django/bin/activate [LINUX]

# 0] clone the repo and switch to the Back-end branch
git clone https://github.com/MarcelloDeSalvo/DeSalvoDubiniGrossoni
git worktree add ../cpms-back-end cpms-back-end
open the new folder inside a terminal or your favourite IDE

# 1] Install the requirements
pip install -r requirements.txt

# 2] Make a .env file inside 'mysite/mysite' (see the next chapter)

# 3] run the server
python manage.py runserver

# 4] test it
http://127.0.0.1:8001

```
## Environment Variables
Inside /mysite/mysite you need to create a .env file containing the following informations (see .env.example for details)

```bash
    SECRET_KEY=your_backend_secret_key
    DATABASE_NAME=your_db_name
    DATABASE_PORT=your_db_port
    DATABASE_USER=your_db_username
    DATABASE_PASSWORD=your_db_password
    DATABASE_URL=your_cloud_db_link
    DEVELOPMENT_MODE=true_or_false
    DEBUG=true_or_false
    ALLOWED_HOSTS=string_list
```


## Development Server

Start the development server on http://127.0.0.1:8001

```bash
python manage.py runserver
```


## Database setup
Install postgresSQL
make a DB with

name = your_db_name  
password = your_db_password  
user = your_db_user_name  
host = your_db_local_url  
port = your_db_port  


```bash
manage.py makemigrations
manage.py migrate
manage.py createsuperuser
```

now you can connect with superuser credentials on http://localhost:8001/admin/
