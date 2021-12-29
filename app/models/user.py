from app import db
from sqlalchemy_utils import PhoneNumber, PhoneNumberType


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  name = db.Column(db.String(120))
  total_budget = db.Column(db.Integer)

  phone_number = db.Column(PhoneNumberType())

  budget_categories = db.relationship("Budget", backref="user", lazy="dynamic")

  __table_args__ = (db.UniqueConstraint('phone_number'),)

  def __repr__(self):
    return f"User {self.name}: phone: {self.phone_number}, email: {self.email}, total budget: {self.total_budget}"
