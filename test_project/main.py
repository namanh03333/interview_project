from flask import Blueprint,render_template
from flask_login import current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():

    return render_template("trangchu.html", user=current_user)


@main.route('/profile')
def profile():
    return 'Profile'