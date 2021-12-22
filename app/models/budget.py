from app import db
from app.models.user import User

class Budget(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), index=True)
  allotted_amount = db.Column(db.Float)
  amount_remaining = db.Column(db.Float)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
  purchases = db.relationship("Purchase", backref="category", lazy="dynamic")

  def __repr__(self):
    return f"{self.name}: total amount: {self.allotted_amount}, amount remaining: {self.amount_remaining}. Owned by User {self.user_id}"