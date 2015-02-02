from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo
from flask.ext.wtf import Form

from .validators import ( CheckPasswd, CheckUser,
                        UserExists, CheckDomain,
                        EmailValid )

ERR_OBLIG = "non-optional field"
ERR_EMAIL = "invalid e-mail address"
ERR_CONFIRM = "passwords must match"
ERR_PASSWD = "invalid password"
ERR_USER = "invalid user"
ERR_DOMAIN = "invalid domain"
ERR_EXISTS = "username taken"

class RegisterForm(Form):

  username = StringField("username",
                        validators=[InputRequired(ERR_OBLIG),
                                    EmailValid(ERR_EMAIL),
                                    CheckDomain(ERR_DOMAIN),
                                    UserExists(ERR_EXISTS) ] )
  passwd = PasswordField("password",
                        validators=[InputRequired(ERR_OBLIG),
                                    EqualTo("confirm", ERR_CONFIRM) ] )
  confirm = PasswordField("confirm",
                        validators=[InputRequired(ERR_OBLIG) ] )
  submit = SubmitField("register")

class PasswdForm(Form):
  username = StringField("username",
                        validators=[InputRequired(ERR_OBLIG),
                                    Email(ERR_EMAIL),
                                    CheckUser(ERR_USER) ] )
  old = PasswordField("old password",
                        validators=[InputRequired(ERR_OBLIG),
                                    CheckUser(ERR_PASSWD),
                                    CheckPasswd(ERR_PASSWD) ] )
  passwd = PasswordField("password",
                        validators=[InputRequired(ERR_OBLIG),
                                    EqualTo("confirm", ERR_CONFIRM) ] )
  confirm = PasswordField("confirm",
                        validators=[InputRequired(ERR_OBLIG) ] )
  submit = SubmitField("change password")

