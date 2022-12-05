from datetime import datetime
from time import time
from pymongo import MongoClient
from flask import Flask, render_template, request
import os
from twilio.rest import Client
from flask_pymongo import PyMongo

app = Flask(__name__)  # creates an instance of flask for us

# mongoDB connection
MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(
    "mongodb+srv://benkluger:Dadsters1@cluster0.4rltfof.mongodb.net/?retryWrites=true&w=majority")  # MONGO_URI)

db = client.get_database('reminderApp_db')
reminders = db.Reminders


subscribers = []
# reminders = []


@app.route('/')  # home or index page
def index():

    # this iterates through all the documents in the Reminders database
    for doc in reminders.find():
        phoneNumber = doc.get("phone")
        timeToRemind = doc.get("time")
        messageToSend = doc.get("message")

        str_time = datetime.timeToRemind.strptime(datetime, "%m/%j/%y %H:%M")
        print(str_time)

    # reminders.insert_one({'name': 'FKJAHSDKF'})
    print('Added a user!')
    return render_template("index.html")


@app.route('/about')
def about():
    names = ["John", "Ben", "Wes", "Sally"]
    return render_template("about.html", names=names)


@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")


@app.route('/subscribeForm', methods=["POST"])
def subscribeForm():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    phone = request.form.get("phone")

    if not first_name or not last_name or not phone:
        error_statement = "All form fields required..."
        return render_template("subscribe.html", error_statement=error_statement,
                               first_name=first_name, last_name=last_name, phone=phone)

    text_to_send = f"{first_name} {last_name} || {phone}"

    # # Find your Account SID and Auth Token at twilio.com/console
    # # and set the environment variables. See http://twil.io/secure
    # account_sid = os.environ.get("ACCOUNT_ID")
    # auth_token = os.environ.get("AUTH_TOKEN")
    # client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #     body=text_to_send,
    #     from_='+19896834418',
    #     to=phone
    # )

    # print(message.sid)

    subscribers.append(f"{first_name} {last_name} || {phone}")
    return render_template("subscribeForm.html", subscribers=subscribers)


@app.route('/reminder')
def reminder():
    return render_template("storeReminder.html")


@app.route('/reminderForm', methods=["POST"])
def reminderForm():
    message = request.form.get("message")
    timeToRemind = request.form.get("timeToRemind")
    phone = request.form.get("phone")

    if not message or not timeToRemind or not phone:
        error_statement = "All form fields required..."
        return render_template("storeReminder.html", error_statement=error_statement,
                               message=message, timeToRemind=timeToRemind, phone=phone)

    text_to_send = f"{phone} has asked to be reminded at {timeToRemind} of: {message}"

    # # Find your Account SID and Auth Token at twilio.com/console
    # # and set the environment variables. See http://twil.io/secure
    # account_sid = os.environ.get("ACCOUNT_ID")
    # auth_token = os.environ.get("AUTH_TOKEN")
    # client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #     body=text_to_send,
    #     from_='+19896834418',
    #     to=phone
    # )

    # print(message.sid)
    # reminders.append(f"{phone} at time {timeToRemind} || {reminder}")
    reminders.insert_one(
        {'phone': phone, 'time': timeToRemind, 'message': message})
    return render_template("reminderForm.html")  # , reminders=reminders)
