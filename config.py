import os
import base64

DATABASE_PATH="/path/to/db"

SECRET_KEY = base64.b64encode(os.urandom(10) )
SQLALCHEMY_DATABASE_URI = "sqlite:///"+DATABASE_PATH
