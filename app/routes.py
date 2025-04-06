from flask import Blueprint, jsonify, request
from app import db
from app.models import Properties, Agents, Buyer, Rent, Sale, Owner

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return "Real Estate Backend Running"


@bp.route('/properties', methods=['GET'])
def get_all_properties():
    properties = Properties.query.all()
    result = []
    for p in properties:
        result.append({
            'property_id': p.property_id,
            'property_name': p.property_name,
            'city': p.city,
            'state': p.state,
            'size_sqf': p.size_sqf,
            'bedrooms': p.no_of_bedrooms,
            'rent_price': float(p.rent_price),
            'sale_price': float(p.sale_price),
            'status': p.status
        })
    return jsonify(result)

# GET all agents
@bp.route('/agents', methods=['GET'])
def get_all_agents():
    agents = Agents.query.all()
    result = []
    for a in agents:
        result.append({
            'agent_id': a.agent_id,
            'email': a.email,
            'phone_number': a.phone_number,
            'first_name': a.first_name,
            'last_name': a.last_name,
            'state': a.state,
            'city': a.city,
            'address_line': a.address_line,
        })
    return jsonify(result)


# GET all owners
@bp.route('/owners', methods=['GET'])
def get_all_owners():
    owners = Owner.query.all()
    result = []
    for o in owners:
        result.append({
            'owner_id': o.owner_id,
            'name': o.name,
            'email': o.email,
            'phone': o.phone,
            'adhar_number': o.adhar_number,
            'state': o.state,
            'city': o.city,
            'address_line': o.address_line,
        })
    return jsonify(result)


# GET all buyers
@bp.route('/buyers', methods=['GET'])
def get_all_buyers():
    buyers = Buyers.query.all()
    result = []
    for b in buyers:
        result.append({
            'buyer_id': b.buyer_id,
            'name': b.name,
            'phone': b.phone,
            'adhar_number': b.adhar_number,
        })
    return jsonify(result)


# GET all rent records
@bp.route('/rents', methods=['GET'])
def get_all_rents():
    rents = Rent.query.all()
    result = []
    for r in rents:
        result.append({
            'id': r.id,
            'property_id': r.property_id,
            'buyer_id': r.buyer_id,
            'agent_id': r.agent_id,
            'rent_price': float(r.rent_price),
            'rent_date': str(r.rent_date),
            'duration_of_rent': r.duration_of_rent,
        })
    return jsonify(result)


# GET all sale records
@bp.route('/sales', methods=['GET'])
def get_all_sales():
    sales = Sale.query.all()
    result = []
    for s in sales:
        result.append({
            'id': s.id,
            'property_id': s.property_id,
            'buyer_id': s.buyer_id,
            'agent_id': s.agent_id,
            'sale_price': float(s.sale_price),
            'sale_date': str(s.sale_date),
        })
    return jsonify(result)
