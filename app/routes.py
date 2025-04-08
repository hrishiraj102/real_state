from flask import Blueprint, jsonify, request
from app import db
from app.models import Properties, Agents, Buyer, Rent, Sale, Owner
from werkzeug.security import check_password_hash, generate_password_hash
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
    if Agents.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Agent already exists'}), 400
    new_agent = Agents(
        email=data['email'],
        phone_number=data['phone_number'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        state=data['state'],
        city=data['city'],
        address_line=data['address_line'],
        password_hash=generate_password_hash(data['password'])
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


#put

@bp.route('/agents/<int:agent_id>', methods=['PUT'])
def update_agent(agent_id):
    agent = Agents.query.get(agent_id)
    if not agent:
        return jsonify({'error': 'Agent not found'}), 404

    data = request.get_json()
    agent.first_name = data.get('first_name', agent.first_name)
    agent.last_name = data.get('last_name', agent.last_name)
    agent.email = data.get('email', agent.email)
    agent.phone_number = data.get('phone_number', agent.phone_number)
    agent.state = data.get('state', agent.state)
    agent.city = data.get('city', agent.city)
    agent.address_line = data.get('address_line', agent.address_line)

    # ✅ Proper password hashing
    if 'password' in data:
        agent.password_hash = generate_password_hash(data['password'])

    db.session.commit()
    return jsonify({'message': 'Agent updated successfully'})

@bp.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    prop = Properties.query.get(property_id)
    if not prop:
        return jsonify({'error': 'Property not found'}), 404

    data = request.get_json()
    prop.owner_id = data.get('owner_id', prop.owner_id)
    prop.agent_id = data.get('agent_id', prop.agent_id)
    prop.property_name = data.get('property_name', prop.property_name)
    prop.state = data.get('state', prop.state)
    prop.city = data.get('city', prop.city)
    prop.address_line = data.get('address_line', prop.address_line)
    prop.size_sqf = data.get('size_sqf', prop.size_sqf)
    prop.no_of_bedrooms = data.get('no_of_bedrooms', prop.no_of_bedrooms)
    prop.year_built = data.get('year_built', prop.year_built)
    prop.rent_price = data.get('rent_price', prop.rent_price)
    prop.sale_price = data.get('sale_price', prop.sale_price)
    prop.status = data.get('status', prop.status)
    prop.date_of_listing = data.get('date_of_listing', prop.date_of_listing)

    db.session.commit()
    return jsonify({'message': 'Property updated successfully'})


@bp.route('/buyers/<int:buyer_id>', methods=['PUT'])
def update_buyer(buyer_id):
    buyer = Buyer.query.get(buyer_id)
    if not buyer:
        return jsonify({'error': 'Buyer not found'}), 404

    data = request.get_json()
    buyer.name = data.get('name', buyer.name)
    buyer.phone = data.get('phone', buyer.phone)
    buyer.adhar_number = data.get('adhar_number', buyer.adhar_number)

    db.session.commit()
    return jsonify({'message': 'Buyer updated successfully'})


@bp.route('/rents/<int:rent_id>', methods=['PUT'])
def update_rent(rent_id):
    rent = Rent.query.get(rent_id)
    if not rent:
        return jsonify({'error': 'Rent record not found'}), 404

    data = request.get_json()
    rent.property_id = data.get('property_id', rent.property_id)
    rent.buyer_id = data.get('buyer_id', rent.buyer_id)
    rent.agent_id = data.get('agent_id', rent.agent_id)
    rent.rent_price = data.get('rent_price', rent.rent_price)
    rent.rent_date = data.get('rent_date', rent.rent_date)
    rent.duration_of_rent = data.get('duration_of_rent', rent.duration_of_rent)

    db.session.commit()
    return jsonify({'message': 'Rent record updated successfully'})


@bp.route('/sales/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id):
    sale = Sale.query.get(sale_id)
    if not sale:
        return jsonify({'error': 'Sale record not found'}), 404

    data = request.get_json()
    sale.property_id = data.get('property_id', sale.property_id)
    sale.buyer_id = data.get('buyer_id', sale.buyer_id)
    sale.agent_id = data.get('agent_id', sale.agent_id)
    sale.sale_price = data.get('sale_price', sale.sale_price)
    sale.sale_date = data.get('sale_date', sale.sale_date)

    db.session.commit()
    return jsonify({'message': 'Sale record updated successfully'})


@bp.route('/owners/<int:owner_id>', methods=['PUT'])
def update_owner(owner_id):
    data = request.get_json()
    owner = Owner.query.get(owner_id)

    if not owner:
        return jsonify({'error': 'Owner not found'}), 404

    # Optional: validate fields before updating
    owner.name = data.get('name', owner.name)
    owner.email = data.get('email', owner.email)
    owner.phone = data.get('phone', owner.phone)
    owner.state = data.get('state', owner.state)
    owner.city = data.get('city', owner.city)
    owner.address_line = data.get('address_line', owner.address_line)

    try:
        db.session.commit()
        return jsonify({'message': 'Owner updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
    
    #login/signup
    
   

@bp.route('/login/agent', methods=['POST'])
def login_agent():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    agent = Agents.query.filter_by(email=email).first()

    if agent and check_password_hash(agent.password_hash, password):
        return jsonify({'message': 'Login successful', 'agent_id': agent.agent_id}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401



@bp.route('/register/agent', methods=['POST'])
def register_agent():
    data = request.get_json()

    if Agents.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Agent already exists'}), 400

    hashed_password = generate_password_hash(data['password'])

    new_agent = Agents(
        email=data['email'],
        phone_number=data['phone_number'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        state=data['state'],
        city=data['city'],
        address_line=data['address_line'],
        password_hash=hashed_password
    )

    try:
        db.session.add(new_agent)
        db.session.commit()
        return jsonify({'message': 'Agent registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
