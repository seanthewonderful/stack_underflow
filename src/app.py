from flask import Flask, redirect, render_template, flash, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from jinja2 import StrictUndefined
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from os import environ


app = Flask(__name__)
app.secret_key = environ["SECRET_KEY"]
app.jinja_env.undefined = StrictUndefined
csrf = CSRFProtect(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=False)