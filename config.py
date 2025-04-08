import os
#from flask_jwt_extended import JWTManager
class Config:
    #SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mamu123123@localhost:3306/RealEstateDB'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
