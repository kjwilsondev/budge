# flask-restplus

## Commands

`make install` : installs both system-packages and python-packages
`make clean` : cleans up the app
`make tests` : runs the all the tests
`make run` : starts the application
`make all` : performs clean-up,installation , run tests , and starts the app.

## Resources

- [Python and Flask Web App](https://www.freecodecamp.org/news/how-to-use-python-and-flask-to-build-a-web-app-an-in-depth-tutorial-437dbfe9f1c6/ "Free Code Camp")

- [Blacklisting JWTS](https://auth0.com/blog/blacklist-json-web-token-api-keys/ "AuthO")

- [Flask-RESTPlus](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#what-is-flask-restplus "Free Code Camp")

- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html "VirtualEnvWrapper Docs")

- [PostgreSQL through SQLAlchemy](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/ "Compose")

## App Structure

The model package contains all database models
The service package contains all business logic
The controller package contains all application endpoints
The util package contains all neccessary utilities

## Run Tests

```os
python manage.py test
```

## Update Packages

Run the following command

```os
pip freeze > requirements.txt
```

## Initiate Database Folder

Initiate a migration folder using init command for alembic to perform the migrations.

```os
python3 manage.py db init
python3 manage.py db migrate --message 'initial database migration'
python3 manage.py db upgrade
```

Should have new sqlLite database
flask_boilerplate_main.db
generated inside main folder

Each time the database model changes,
repeat the migrate and upgrade commands

## Virtual Env Commands

Create Env

```os
mkproject [name]
```

List all Envs

```os
ls $WORKON_HOME
```

Reactivate Env

```os
workon [name]
```

Delete Env

```os
rmvirtualenv [name]
```

### Neccessary Packages

- **Flask-bcrypt**
  - for hashing passwords and tokens
- **flask-restplus**
  - formats objects to JSON automatically
- **Flask-Migrate**
  - SQLAlchemy database migrations
  - Flask-Migrate exposes two classes, Migrate and MigrateCommand.
    - Migrateclass contains all the functionality of the extension.
    - MigrateCommand class is used when to expose database migration commands
- **pyjwt**
  - python library for encoding JWT tokens
  - MAKE SURE YOU HAVE PyJWT AND NOT jwt !!!
- **Flask-Script**
- **flask_testing**

### Git Branching

<https://stackoverflow.com/questions/2862590/how-to-replace-master-branch-in-git-entirely-from-another-branch>

## Database Creation

Import

```os
pip install flask-sqlalchemy
brew install postgres
which createdb
```

Create and start db

```os
initdb new-db
pg_ctl -D budget-db -l logfile start
```