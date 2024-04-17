from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('login', required=True,type=str)
parser.add_argument('password', required=True, type=str)
