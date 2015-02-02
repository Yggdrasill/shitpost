from wtforms.validators import StopValidation, Email

from shitpost import db

from .security import verify_passwd
from .models import User, Domain
from .string import verify_email

class CheckPasswd(object):

  def __init__(self, message=None):
    self.message = message

  def __call__(self, form, field):
    user = User.query.filter_by(email=form.username.data.lower() ).first()
    verify = verify_passwd(form.old.data, user.password)

    if self.message == None:
      message = field.gettext("This password is invalid.")
    else:
      message = self.message

    if verify == False:
      raise StopValidation(message)

class CheckUser(object):

  def __init__(self, message=None):
    self.message = message

  def __call__(self, form, field):
    user = User.query.filter_by(email=form.username.data.lower() ).first()

    if self.message == None:
      message = field.gettext("This user doesn't exist.")
    else:
      message = self.message

    if user == None:
      raise StopValidation(message)

class UserExists(object):

  def __init__(self, message=None):
    self.message = message

  def __call__(self, form, field):
    user = User.query.filter_by(email=form.username.data.lower() ).first()

    if self.message == None:
      message = field.gettext("This username is taken.")
    else:
      message = self.message

    if user != None:
      raise StopValidation(message)

class CheckDomain(object):

  def __init__(self, message=None):
    self.message = message

  def __call__(self, form, field):

    result = verify_email(form.username.data.lower() )
    name = result.group(2)
    domain = Domain.query.filter_by(name=name).first()

    if self.message == None:
      message = field.gettext("This domain is unavailable.")
    else:
      message = self.message

    if domain == None:
      raise StopValidation(message)

class EmailValid(object):
  """
  This class was defined only because wtforms Email() validator doesn't raise
  StopValidation, but rather raises ValidationError, which doesn't stop the
  validation, causing CheckDomain() to fail.
  """


  def __init__(self, message=None):
    self.message = message

  def __call__(self, form, field):
    if self.message == None:
      message = field.gettext("Invalid email address.")
    else:
      message = self.message

    result = verify_email(form.username.data.lower() )

    if result == None:
      raise StopValidation(message)

    email = result.group(0)
    user = result.group(1)
    domain = result.group(2)

    if email == None or user == None or domain == None:
      raise StopValidation(message)
