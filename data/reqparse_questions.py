from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('question_id', required=True,type=int)
parser.add_argument('question', required=True,type=str)
parser.add_argument('type', required=True, type=str)
parser.add_argument('answer_options', required=True, type=str)
parser.add_argument('answer', required=True,type=str)
parser.add_argument('owner_id', required=True, type=int)
parser.add_argument('is_public', required=True, type=bool)
