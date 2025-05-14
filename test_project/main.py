from flask import Blueprint, render_template
from flask_login import current_user, login_required
from test_project.models import Category
from . import db

main = Blueprint("main", __name__)


@main.route("/dashboard")
@login_required
def home():
    categories = Category.query.all()
    return render_template("trangchu.html", categories=categories, user=current_user)


@main.route("/profile")
@login_required
def pf():
    return render_template("gioithieu.html", user=current_user)
