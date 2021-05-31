from flask import Flask, flash, redirect, render_template, request, session, abort, make_response
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import uuid
from datetime import datetime
import random
from flask_bootstrap import Bootstrap



app = Flask(__name__)


uuids = [uuid.uuid4() for i in [0,1,2,3,4]]



@app.route('/')
def index():
    return 'Hello, World!'

@app.route("/patienter")
def patienter():
    return render_template("patienter.html", patients=make_zombie_positions())




@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.password.data == "cPq216":
        return redirect('/forside')
    return render_template('login.html', form=form)



@app.route("/forside", methods=['GET', 'POST'])
def forside():
    return render_template('frontpage.html')



@app.route("/id", methods=['GET', 'POST'])
def id():
    form = IDCardForm(request.form)
    if form.username.data == "Helen Smith":
        return render_template('printer_idkort.html')
    return render_template('id_register.html', form=form)



app.secret_key = 'many random bytes'
app.run(host='0.0.0.0', port=8080)


class IDCardForm(Form):
    username = StringField('Navn', [validators.Length(min=4, max=25)])
    title = StringField('Titel', [validators.Length(min=6, max=35)])



class LoginForm(Form):
    password = StringField('Password', [validators.Length(min=4, max=25)])





def make_zombie_positions():
    zombies = f"""
    <p>
    <br>K 1078, rfid {uuids[0]} 
    <br>Ellen Anja Jensen f. 1985-03-09, d. 2021-05-06
    <br>{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} p. G6 E9 I8 E9 - h.bpm. {random.randint(14,21)} - brpm 0
    
    <p>
    <br>K 1034, rfid {uuids[1]} 
    <br>Jesper Nygaard f. 1962-11-02, d. 2021-05-12
    <br>{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} p. L10 L10 L11 L11 - h.bpm. {random.randint(26,32)} - brpm 0
    
    <p>
    <br>K 1089, rfid {uuids[2]} 
    <br>Freja Solblomst Mathiasen f. 2002-02-02, d. 2021-05-22
    <br>{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} p. C3 C5 E5 E3 - h.bpm. {random.randint(23,29)} - brpm 0
    
    <p>
    <br>K 1009, rfid {uuids[3]} 
    <br>Henrik Kreutzen f. 1992-09-24, d. 2021-04-29
    <br>{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} p. E9 E9 E9 E9 - h.bpm. {random.randint(41,45)} - brpm 0
    
    <p>
    <br>K 1008, rfid {uuids[4]} 
    <br>Thorbjørn Olsson f. 1976-05-21, d. 2021-05-25
    <br>{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} p. B14 D13 D15 F14  - h.bpm. {random.randint(31,36)} - brpm 0

    """

    return zombies
