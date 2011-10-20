# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from google.appengine.api import users
from wsgiref.handlers import CGIHandler
import models
import logging 
import json

app = Flask(__name__)
app.debug = True
app.secret_key = "FADSFAS"

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/save/", methods=['GET', 'POST'])
def save():
#    user = users.get_current_user()
    
#    if user:
    
    if request.method == 'POST':
    
        has_child =  request.form['has_child'] == 'true' \
            if 'has_child' in request.form else False

        title = request.form['title'] if 'title' in request.form else None
    
        if title is None or len(title) == 0:
            flash(u'<strong>¡ups!<strong> Debes ingresar un titulo para registrate', 'error') 
        else:
            data = models.Data(title = title, has_child = has_child)
            data.put()
            flash(u'<strong>¡Enhorabuena!<strong> Tus datos han sido guardados', 'success') 

        return render_template("form.html")
    else:
        return render_template("form.html")
            
#    else:
        
#        return redirect(users.create_login_url(url_for('save')))
        

@app.route("/get_all/")
def get_all():
    data = map(lambda x:{ 'title':x.title, 'has_child':x.has_child }, models.Data.all())
    logging.info(data)
    return jsonify(result=data)
    
@app.route("/about/")
def about():
    return render_template("about.html")
    
#@app.route("/logout/")
#def logout():
#    return redirect(users.create_logout_url(url_for('index')))
    
#@app.context_processor
#def init_tempalte():
#    return dict(current_user=users.get_current_user())

if __name__ == '__main__':
    CGIHandler().run(app)

    
