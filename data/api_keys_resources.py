from flask import jsonify
from flask_restful import Resource, abort

from data import db_session
from data.api_keys import Api_keys
from data.questions import Questions
from data.reqparse_api_keys import parser
from werkzeug.security import generate_password_hash, check_password_hash
from secrets import token_urlsafe
def abort_if_login_not_found(login):
    session = db_session.create_session()
    api_key = session.query(Api_keys).filter(Api_keys.login==login).first()
    if not api_key:
        abort(404, message=f"login {login} not found")
def abort_if_password_incorrect(login,password):
    session = db_session.create_session()
    api_key = session.query(Api_keys).filter(Api_keys.login==login).first()
    if not check_password_hash(api_key.hashed_password,password):
        abort(400, message=f"password incorrect")

class ApiKeyResourse(Resource):
    def get(self):
        args = parser.parse_args()
        abort_if_login_not_found(args['login'])
        abort_if_password_incorrect(args['login'],args['password'])
        session = db_session.create_session()
        api_key = session.query(Api_keys).filter(Api_keys.login==args['login']).first()
        return jsonify({'api_key': api_key.to_dict()['api_key']})
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        api_key = session.query(Api_keys).filter(Api_keys.login == args['login']).first()
        if api_key:
            abort(400, message=f"account with login {args['login']} already registred")
        api_key = Api_keys(
            login = args['login'],
            hashed_password = generate_password_hash(args['password']),
            api_key = token_urlsafe(100))
        session.add(api_key)
        token = api_key.api_key
        session.commit()
        session.close()
        return jsonify({'api_key': token})
    def delete(self):
        args = parser.parse_args()
        abort_if_login_not_found(args['login'])
        abort_if_password_incorrect(args['login'], args['password'])
        session = db_session.create_session()
        api_key = session.query(Api_keys).filter(Api_keys.login == args['login']).first()
        questions = session.query(Questions).filter(Questions.api_access_key== api_key.api_key).all()
        for i in questions:
            session.delete(i)
        session.delete(api_key)
        session.commit()
        session.close()
        return jsonify({'success': 'OK'})


