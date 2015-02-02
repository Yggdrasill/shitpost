import re

def verify_email(email):
  pattern = re.compile("^([A-Z0-9-_\.\+]+)@([A-Z0-9-\.]+)", re.IGNORECASE)
  result = pattern.search(email)
  return result

