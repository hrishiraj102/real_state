# # app/auth.py
# import jwt
# from functools import wraps
# from flask import request, jsonify, current_app
# from app.models import Agent, OfficeStaff
# from app import db

# def token_required(role):
#     def decorator(f):
#         @wraps(f)
#         def decorated_function(*args, **kwargs):
#             token = None
#             if 'Authorization' in request.headers:
#                 auth_header = request.headers['Authorization']
#                 if auth_header.startswith('Bearer '):
#                     token = auth_header.split(' ')[1]

#             if not token:
#                 return jsonify({'message': 'Token is missing!'}), 401

#             try:
#                 data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
#                 user_id = data['id']
#                 user_role = data['role']

#                 if user_role != role:
#                     return jsonify({'message': 'Unauthorized access!'}), 403

#                 # Attach current user info to request context if needed
#                 if role == 'agent':
#                     request.current_user = Agent.query.get(user_id)
#                 elif role == 'office':
#                     request.current_user = OfficeStaff.query.get(user_id)

#             except Exception as e:
#                 return jsonify({'message': 'Token is invalid or expired!', 'error': str(e)}), 401

#             return f(*args, **kwargs)
#         return decorated_function
#     return decorator

# # Shortcut decorators
# agent_required = token_required('agent')
# office_required = token_required('office')
