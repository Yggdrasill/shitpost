import base64
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf.csrf import CsrfProtect

shitpost = Flask(__name__)
shitpost.config.from_object("config")

db = SQLAlchemy(shitpost)
csrf = CsrfProtect(shitpost)

from shitpost import main
