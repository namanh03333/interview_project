from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from test_project.form import Login, Signup, Forget_PassWord
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import (
    login_user,
    login_required,
    logout_user,
    current_user,
    LoginManager,
)
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        user_name = form.user_name.data
        password = form.user_password.data

        user = User.query.filter_by(user_name=user_name).first()

        if user:
            if check_password_hash(user.password, password):
                session["user_name"] = user.user_name
                flash("Login Successfull", category="success")
                login_user(user, remember=True)
                return redirect(url_for("main.home"))
            else:
                flash("Incorrect password, please try again", category="error")

        if user is None:
            flash("User does not exist", category="error")
    return render_template("dangnhap.html", form=form, user=current_user)


@auth.route("/dangki", methods=["GET", "POST"])
def signup():
    form = Signup()

    if form.validate_on_submit():
        new_user_name = form.new_user_name.data
        new_user_email = form.new_user_email.data
        new_user_password = form.new_user_password.data
        confirmed_pass = form.confirmed_password.data

        email_exists = User.query.filter_by(email=new_user_email).first()
        user_name_exists = User.query.filter_by(user_name=new_user_name).first()
        if email_exists:
            flash("Email is already exists", category="error")
        elif user_name_exists:
            flash("User is already exists", category="error")
        else:
            if new_user_password == confirmed_pass:
                new_user = User(
                    email=new_user_email,
                    user_name=new_user_name,
                    password=generate_password_hash(new_user_password),
                )
                db.session.add(new_user)
                db.session.commit()
                flash("Account created !!!", category="success")
                return redirect(url_for("auth.login"))

    return render_template("dangki.html", form=form, user=current_user)


@auth.route("/quenMK",methods=['GET','POST'])
def forget_password():
    form = Forget_PassWord()
    if form.validate_on_submit():
        user_name = form.user_name.data
        user_email = form.user_email.data
        new_password = form.new_user_password.data
        confirmed_password = form.confirmed_password.data
        if new_password == confirmed_password:
            user = User.query.filter_by(user_name=user_name, email=user_email).first()
            if user:
                user.password = generate_password_hash(new_password)
                db.session.commit()
                flash("Reset PassWord Successful!!", "success")
                return redirect(url_for("auth.login"))
            else:
                flash("Error", "danger")
    else:
        flash("Password does not match", "warning")

    return render_template("quenMK.html", form=form, user=current_user)


@auth.route("/logout", methods=["POST", "GET"])
def logout():
    if request.method == "POST":
        logout_user()
        return redirect(url_for("auth.login"))

    return render_template("trangchu.html", user=current_user)
