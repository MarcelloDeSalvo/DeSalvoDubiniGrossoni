# Django Minimal Starter

Look at https://docs.djangoproject.com/en/4.1/intro/tutorial01/ to learn more.
Look at https://docs.digitalocean.com/tutorials/app-deploy-django-app/ to learn how to deploy django on Digital Ocean

mettere link host

## Local Setup

Make sure to have the dependencies and Python (>= 3.9.12) installed:

```bash
# 0] Upgrade pip if necessary
python -m pip install --upgrade pip

# 1] create a virtual environment with your favourite env. manager (in this ex. venv)
python -m venv django

# 2] activate the environment
django\Scripts\activate.bat

# 3] clone the repo and switch to the Back-end branch
git clone https://github.com/MarcelloDeSalvo/DeSalvoDubiniGrossoni
git worktree add ../emsp-back-end esmp-back-end
open the new folder

# 4] Install the requirements
pip install -r requirements.txt

# 5] Make a .env file inside 'mysite/mysite' (see the next chapter)

# 6] run the server
python manage.py runserver

# 7] test it
http://127.0.0.1:8000

```
## Environment Variables
Inside /mysite/mysite you need to create a .env file containing the following informations

```bash
SECRET_KEY=your_backend_secret_key
DATABASE_NAME=your_db_name
DATABASE_PORT=your_db_port
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password

DATABASE_URL=your_db_url
DEVELOPMENT_MODE=True if working locally, False otherwise
DEBUG=True/False
ALLOWED_HOSTS="localhost domain1 domain2 etc.." or "*" to allow all possible domains
```


## Development Server

Start the development server on http://127.0.0.1:8000

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
manage.py createsuperuser -> follow instructions
```

now you can connect with superuser credentials on http://localhost:8000/admin/