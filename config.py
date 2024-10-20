import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/ems_user'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # For session management
