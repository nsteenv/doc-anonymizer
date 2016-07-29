# config.py


import os

class BaseConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']
    UPLOAD_FOLDER = os.environ['UPLOAD_FOLDER']
    PROCESSED_FOLDER = os.environ['PROCESSED_FOLDER']

# Debug mode
# class BaseConfig(object):
#     SECRET_KEY = "Hello"
#     DEBUG = True
#     UPLOAD_FOLDER = "input"
#     PROCESSED_FOLDER = "output"