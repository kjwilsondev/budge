from .. import db, flask_bcrypt
import datetime
from ..config import key

# Budget class inherits from db.Model class which declares the class as a model for sqlalchemy
class Budget(db.Model):
    """ Budget Model for storing budget related details """
    __tablename__ = "budget"

    # Budget fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    set_on = db.Column(db.DateTime, nullable=False)
    length = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    success = db.Column(db.Boolean, nullable=False)

    # Relationships
    public_id = db.Column(db.String, db.ForeignKey('user.public_id'))
    # user = db.relationship("User", backref=db.backref("budgets", order_by="desc(Budget.set_on)"))
