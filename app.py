from flask import Flask, flash, redirect, render_template, request, session, abort
from wtforms import Form, BooleanField, StringField, PasswordField, validators



app = Flask(__name__)


id_cards = {"Tue": "Talnørd",
"Aske": "Professionel bøf",
"Amalie": "pole"}



@app.route('/')
def index():
    return 'Hello, World!'

@app.route("/chiptracker")
def chiptracker():
    return "Members"

@app.route("/id", methods=['GET', 'POST'])
def id():
    form = IDCardForm(request.form)
    if form.username.data in id_cards:
        if id_cards[form.username.data] == form.title.data:
            return 'ALT ER GODT'
    return render_template('id_register.html', form=form)


@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
    'test.html',name=name)


app.run(host='0.0.0.0', port=8080)


class IDCardForm(Form):
    username = StringField('Navn', [validators.Length(min=4, max=25)])
    title = StringField('Titel', [validators.Length(min=6, max=35)])
