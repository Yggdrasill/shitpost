import os
import hashlib
import base64

def hash_ssha512(passwd, salt):
  sha = hashlib.sha512()
  sha.update(passwd.encode("utf-8") )
  sha.update(salt)
  ssha512 = base64.b64encode(sha.digest()+salt)

  return "{SSHA512}" + ssha512.decode("utf-8")

def hash_passwd(passwd):
  return hash_ssha512(passwd, os.urandom(5) )

def verify_passwd(passwd, ssha512):
  decode = base64.b64decode(ssha512[9:])
  salt = decode[64:]

  return hash_ssha512(passwd, salt) == ssha512
