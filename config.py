import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
url = os.environ.get('FYYUR_POSTGRES_URL')
if url is not None and len(url) > 0:
    SQLALCHEMY_DATABASE_URI = url
else:
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:password@localhost:5432/fyyur'

# Disable tracking modifications to eliminate warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
