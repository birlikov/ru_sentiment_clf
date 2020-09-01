# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators

from utils import get_sentiment

app = Flask(__name__)
app.secret_key = os.urandom(24)

class ResusableForm(Form):
    textfield = TextField('text', validators=[validators.required()])

@app.route("/", methods = ['GET','POST'])
def main_function():
    form = ResusableForm(request.form)
    if request.method == 'POST':
        text = request.form['textfield']
        sentiment, score = get_sentiment(text)
        flash(f'text: {text}')
        flash(f'sentiment: {sentiment}, score: {score}')
    return render_template('main_template.html', form = form)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=80)