#!/usr/bin/env python

from shitpost import db

class Domain(db.Model):
  __tablename__ = "virtual_domains"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, unique=True)
  users = db.relationship("User", backref="domain")
  aliases = db.relationship("Alias", backref="domain")

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "<Domain %r>" % self.name

class User(db.Model):
  __tablename__ = "virtual_users"
  id = db.Column(db.Integer, primary_key=True)
  domain_id = db.Column(db.Integer, db.ForeignKey("virtual_domains.id") )
  email = db.Column(db.String(254), unique=True)
  password = db.Column(db.Text, unique=True)
  active = db.Column(db.Boolean)
  created = db.Column(db.String(30) )
  modified = db.Column(db.String(30) )
  aliases = db.relationship("Alias", backref="user")

  def __init__(self, domain_id, email, password, active, created, modified):
    self.domain_id = domain_id
    self.email = email
    self.password = password
    self.active = active
    self.created = created
    self.modified = modified

  def __repr__(self):
    return "<User %r>" % self.email

class Alias(db.Model):
  __tablename__ = "virtual_aliases"
  id = db.Column(db.Integer, primary_key=True)
  domain_id = db.Column(db.Integer, db.ForeignKey("virtual_domains.id") )
  dest_id = db.Column(db.Integer, db.ForeignKey("virtual_users.id") )
  source = db.Column(db.String(254), unique=True)
  created = db.Column(db.String(30) )
  modified = db.Column(db.String(30) )

  def __init__(self, domain_id, dest_id, source, created, modified):
    self.domain_id = domain_id
    self.dest_id = dest_id
    self.source = source
    self.created = created
    self.modified = modified

  def __repr__(self):
    return "<Alias %r>" % self.source
