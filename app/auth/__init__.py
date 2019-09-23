from flask import Blueprint
from app.auth import forms

auth = Blueprint('auth',__name__)

from . import views,forms