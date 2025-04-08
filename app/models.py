from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Agents(db.Model):
    __tablename__ = 'Agents'
    agent_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    state = db.Column(db.Enum('Assam', 'West Bengal', 'Delhi'))
    city = db.Column(db.Enum('Guwahati', 'Kolkata', 'Delhi'))
    address_line = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Owner(db.Model):
    __tablename__ = 'Owner'
    owner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(20))
    adhar_number = db.Column(db.String(12), unique=True, nullable=False)
    state = db.Column(db.Enum('Assam', 'West Bengal', 'Delhi'))
    city = db.Column(db.Enum('Guwahati', 'Kolkata', 'Delhi'))
    address_line = db.Column(db.String(255))

class Properties(db.Model):
    __tablename__ = 'Properties'
    property_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('Owner.owner_id'))
    agent_id = db.Column(db.Integer, db.ForeignKey('Agents.agent_id'))
    property_name = db.Column(db.String(50), unique=True)
    state = db.Column(db.Enum('Assam', 'West Bengal', 'Delhi'))
    city = db.Column(db.Enum('Guwahati', 'Kolkata', 'Delhi'))
    address_line = db.Column(db.String(255))
    size_sqf = db.Column(db.Integer)
    no_of_bedrooms = db.Column(db.Integer)
    year_built = db.Column(db.Integer)
    rent_price = db.Column(db.Numeric(10, 2))
    sale_price = db.Column(db.Numeric(10, 2))
    status = db.Column(db.Enum('Available', 'Rented', 'Sold'))
    date_of_listing = db.Column(db.Date)

class Buyer(db.Model):
    __tablename__ = 'Buyer'
    buyer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    adhar_number = db.Column(db.String(12), unique=True, nullable=False)

class Rent(db.Model):
    __tablename__ = 'Rent'
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('Properties.property_id', ondelete='CASCADE'), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('Buyer.buyer_id', ondelete='CASCADE'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('Agents.agent_id', ondelete='CASCADE'), nullable=False)
    rent_price = db.Column(db.Numeric(10, 2))
    rent_date = db.Column(db.Date)
    duration_of_rent = db.Column(db.Integer)

class Sale(db.Model):
    __tablename__ = 'Sale'
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('Properties.property_id', ondelete='CASCADE'), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('Buyer.buyer_id', ondelete='CASCADE'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('Agents.agent_id', ondelete='CASCADE'), nullable=False)
    sale_price = db.Column(db.Numeric(10, 2))
    sale_date = db.Column(db.Date)
