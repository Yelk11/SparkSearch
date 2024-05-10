from flask import Flask, render_template, request
from . import db

import os

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.debug = True
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/', methods =["GET", "POST"])
    def searchbar():
        # if request.method == "POST":
        #     search_form = request.form.get("search_form")
        #     return "Your name is " + search_form
        return render_template('new_index.html')

    
    db.init_app(app)

    return app

