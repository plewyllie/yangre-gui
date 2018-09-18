#Author: Pieter Lewyllie, pilewyll@cisco.com
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
