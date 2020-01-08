# Model

## Flask SQLAlquemy

[One to Many Docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships)

## Budget Model

```py
# Budget id
id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# Budget set up date for listing budgets in order
set_on = db.Column(db.DateTime, nullable=False)
# Budget time length
length = db.Column(db.String, nullable=False)
# Budget amount
amount = db.Column(db.Float, nullable=False)
# Budget success tracker
# whether or not user spent less than budget
success = db.Column(db.Boolean, nullable=False)
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

```os
python3 manage.py db stamp heads
python3 manage.py db migrate --message
python3 manage.py db upgrade
```

### Migration Issues

[When I Tried Migrating After Changing and Adding Models](https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date)
