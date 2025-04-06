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


#Post 

@bp.route('/properties', methods=['POST'])
def create_property():
    data = request.json
    new_property = Properties(
        owner_id=data['owner_id'],
        agent_id=data['agent_id'],
        property_name=data['property_name'],
        state=data['state'],
        city=data['city'],
        address_line=data['address_line'],
        size_sqf=data['size_sqf'],
        no_of_bedrooms=data['no_of_bedrooms'],
        year_built=data['year_built'],
        rent_price=data['rent_price'],
        sale_price=data['sale_price'],
        status=data['status'],
        date_of_listing=data['date_of_listing']
    )
    db.session.add(new_property)
    db.session.commit()
    return jsonify({'message': 'Property added successfully'}), 201


@bp.route('/agents', methods=['POST'])
def create_agent():
    data = request.json
    new_agent = Agents(
        email=data['email'],
        phone_number=data['phone_number'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        state=data['state'],
        city=data['city'],
        address_line=data['address_line'],
        password_hash=data['password_hash']
    )
    db.session.add(new_agent)
    db.session.commit()
    return jsonify({'message': 'Agent added successfully'}), 201


@bp.route('/owners', methods=['POST'])
def create_owner():
    data = request.json
    new_owner = Owner(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        adhar_number=data['adhar_number'],
        state=data['state'],
        city=data['city'],
        address_line=data['address_line']
    )
    db.session.add(new_owner)
    db.session.commit()
    return jsonify({'message': 'Owner added successfully'}), 201


@bp.route('/buyers', methods=['POST'])
def create_buyer():
    data = request.json
    new_buyer = Buyer(
        name=data['name'],
        phone=data['phone'],
        adhar_number=data['adhar_number']
    )
    db.session.add(new_buyer)
    db.session.commit()
    return jsonify({'message': 'Buyer added successfully'}), 201


@bp.route('/rents', methods=['POST'])
def create_rent():
    data = request.json
    new_rent = Rent(
        property_id=data['property_id'],
        buyer_id=data['buyer_id'],
        agent_id=data['agent_id'],
        rent_price=data['rent_price'],
        rent_date=data['rent_date'],
        duration_of_rent=data['duration_of_rent']
    )
    db.session.add(new_rent)
    db.session.commit()
    return jsonify({'message': 'Rent record added successfully'}), 201


@bp.route('/sales', methods=['POST'])
def create_sale():
    data = request.json
    new_sale = Sale(
        property_id=data['property_id'],
        buyer_id=data['buyer_id'],
        agent_id=data['agent_id'],
        sale_price=data['sale_price'],
        sale_date=data['sale_date']
    )
    db.session.add(new_sale)
    db.session.commit()
    return jsonify({'message': 'Sale record added successfully'}), 201
