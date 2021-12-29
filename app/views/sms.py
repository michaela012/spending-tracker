from flask import render_template, Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PhoneNumber
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from app import app
from app.models.user import User


@app.route('/sms')
def sms():
  user = {'username': "sms page"}
  account_sid = app.config["TWILIO_ACCOUNT_SID"]
  auth_token = app.config["TWILIO_AUTH_TOKEN"]
  messaging_service_sid = app.config["TWILIO_MESSAGING_SERVICE_SID"]
  client = Client(account_sid, auth_token)

  message = client.messages.create(
    messaging_service_sid=messaging_service_sid,
    body="test message2",
    to="+17175384815"
    )

  return render_template('index.html', title='Home', user=user)


@app.route('/sms/test', methods=["POST"])
def sms_test():
  body = request.values.get('Body', None)
  number = PhoneNumber(request.values.get('From'))
  resp = MessagingResponse()

  user = User.query.filter_by(phone_number=number).first()

  print(f"num: {number}")
  print(user)
  print(body)

  if body == 'hello':
    resp.message("Hi!")
  elif body == 'bye':
    resp.message("Goodbye")
  else:
    resp.message(f"\n\nHey @{str(number)}! Why are you texting me >:(")

  return str(resp)
