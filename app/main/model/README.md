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
