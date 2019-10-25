import os

class Config:
    SECRET_KEY = 'd1cb6705b8834bd8c206e10403b0c8ea'
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT='587'
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')