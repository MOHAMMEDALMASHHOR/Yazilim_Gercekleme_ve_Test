import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///task_management.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False