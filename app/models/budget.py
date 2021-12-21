from app import db
from app.models.user import User

class Budget(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), index=True)
  allotted_amount = db.Column(db.Integer)
  amount_remaining = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey(user.id))

  def __repr__(self):
    return f"{self.name}: total amount: {self.allotted_amount}, amount remaining: {self.amount_remaining}. Owned by User {self.user_id}"