import os
from dotenv import load_dotenv
load_dotenv()


class Config:
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql://user:pass@localhost/marketpro')
SQLALCHEMY_TRACK_MODIFICATIONS = False
PLOTLY_OFFLINE = True


config = Config()