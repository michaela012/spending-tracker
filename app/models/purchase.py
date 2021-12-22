from datetime import datetime
from app import db
from app.models.user import User
from app.models.budget import Budget

class Purchase(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.Text)
  amount = db.Column(db.Float)
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
  category_id = db.Column(db.Integer, db.ForeignKey("budget.id"))

  def __repr__(self):
    return f"{self.description}: ${self.amount} at ${self.timestamp}"