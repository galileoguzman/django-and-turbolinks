# Django + Turbolinks

This project takes you step by step to implement Turbolinks into a Django project.

### Operating System Dependencies

This project uses next dependencies:

- Python 3.8
- PostgreSQL 12 or newer

### Virtual environment

After clone this repository you shall create your virtual environment, I strong recommend you do it with `venv` module inside `python3.5>` like this.

```
python3 -m venv .venv
```

This repository ignore a `virtualenv` named `.venv` as convention.

Do not forget activate it

```
source .venv/bin/activate
```

or if you are using a Windows system

```
.venv\Scripts\activate
```

### Install requirements

After create your virtual environment you have to install the project requirements from `requirements.txt` file.

```
pip install -r requirements.txt
```

### Database

We are using PostgreSQL, here you will find how create a database with this engine.

```
CREATE USER your_db_user PASSWORD 'your_db_user_psw';
ALTER ROLE your_db_user WITH SUPERUSER;
CREATE DATABASE your_db_name WITH OWNER your_db_user;
```

For database connection we are using [dj-database-url](https://pypi.org/project/dj-database-url/).

### Settings

Set your environment variables using the next template. We use [python-decouple](https://pypi.org/project/python-decouple/) to handle our secrets so you only need to create a file named `.env` at the root of your project.

```
# APPLICATION MODE
DEBUG=True # False for production

# DATABASE CONNECTION
DATABASE_URL=postgres://your_db_user:your_db_user_psw@your_db_host:your_db_host_port/your_db_name

# MAIN KEY CIPHER
SECRET_KEY=YOUR_STRONG_SECRET_KEY
```


### Run the project

After you made the above steps, you will be able to run the project, do not forget run the migrations command.

```
python manage.py migrate
python manage.py run server
```
