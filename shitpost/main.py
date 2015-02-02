import datetime

from flask import ( request, render_template,
                flash, redirect, session, abort )

from shitpost import shitpost, db

from .forms import RegisterForm, PasswdForm
from .models import Domain, User, Alias
from .constants import HEADER
from .security import hash_passwd, verify_passwd

db.create_all()

@shitpost.route("/")
def shitpost_home():
  return render_template("index.html", title=HEADER+" - home", page="home")

@shitpost.route("/info")
def shitpost_info():
  return render_template("info.html", title=HEADER+" - info",
                        page="information")

@shitpost.route("/success")
def shitpost_success():
  return render_template("success.html", title=HEADER+" - success",
                        page="success")

@shitpost.route("/register", methods=["POST", "GET"])
def register_user():
  form = RegisterForm()
  if request.method == "POST" and form.validate_on_submit():
    password = hash_passwd(form.passwd.data)
    user = User(1, form.username.data.lower(), password, 0,
                str(datetime.datetime.now()), str(datetime.datetime.now()))
    db.session.add(user)
    db.session.commit()
    flash("registered")
    return redirect("/success")
  return render_template("register.html", title=HEADER+" - register",
                        page="register", form=form)

@shitpost.route("/passwd", methods=["POST", "GET"])
def passwd_user():
  form = PasswdForm()
  if request.method == "POST" and form.validate_on_submit():
    user = User.query.filter_by(email=form.username.data.lower() ).first()
    passwd = hash_passwd(form.passwd.data)
    user.password = str(passwd)
    user.modified = str(datetime.datetime.now() )
    db.session.commit()
    return redirect("/success")

  return render_template("passwd.html", title=HEADER+" - change password",
                        page="change password", form=form)

