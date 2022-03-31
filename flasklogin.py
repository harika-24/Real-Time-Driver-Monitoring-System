from flask_bootstrap import Bootstrap
from flask import Flask, flash, redirect, render_template, request, session, abort
import os


app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello boss"

@app.route('/login',methods=['GET'])
def do_admin_login():
    if request.form['passwordS']=='password' and request.form['username']=='admin':
        session['logged_in']=True
    else:
        flash('wrong password!')
    return home()

if __name__=="__main__":
    app.secret_key ="vhydgjhgdfgC"
    app.run(debug=True,host='0.0.0.0',port=4000)


