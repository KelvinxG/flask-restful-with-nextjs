# resources/user_resource.py

from flask_restful import Resource, reqparse
from backend.models.user import User
from backend import db  # Assuming db is your SQLAlchemy instance

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username is required')
parser.add_argument('email', type=str, required=True, help='Email is required')
parser.add_argument('password', type=str, required=True, help='Password is required')

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user.serialize()

    def post(self):
        args = parser.parse_args()
        new_user = User(username=args['username'], email=args['email'], password=args['password'])
        db.session.add(new_user)
        db.session.commit()
        return new_user.serialize(), 201

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        args = parser.parse_args()
        user.username = args.get('username', user.username)
        user.email = args.get('email', user.email)
        user.password = args.get('password', user.password)
        db.session.commit()
        return user.serialize()

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
