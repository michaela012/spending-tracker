from app import db

class Budget(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  name = db.Column(db.String(120))
  total_budget = db.Column(db.Integer)
  _phone_number = db.Column(db.Unicode(20), nullable=False)
  phone_country_code = db.Column(db.Unicode(8))

  phone_number = db.composite(
    PhoneNumber,
    _phone_number,
    phone_country_code
  )



  def __repr__(self):