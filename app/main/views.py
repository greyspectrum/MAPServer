from flask import render_template, session, redirect, url_for, current_app, g
from . import main

from sqlalchemy import select 
from mapsdb import schema

from app.db import get_db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/transitions')
def transitions():
    # transitions_list = ["C18O", "13CO", "buttermilk"]

    s = select([schema.transitions])
    db = get_db()
    result = db.execute(s)
    transitions_list = result.fetchall()

    return render_template('transitions.html', transitions=transitions_list)