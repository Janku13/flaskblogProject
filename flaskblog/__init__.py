# set FLASK_ENV=development
# set FLASK_APP=.py
# this file makes the site db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# to protect the cookies (use the import secrets to get key) secets.token.hex(16)
app.config["SECRET_KEY"] = "ff2a04c7a9d042f9a20775508cd1e96f"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

# in the end so that we dont have circle importing
from flaskblog import routes
