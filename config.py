import os

class Config:
    #SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mamu123123@localhost:3306/RealEstateDB'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
