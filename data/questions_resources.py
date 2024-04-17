from flask import jsonify
from flask_restful import Resource, abort

from data import db_session
from data.questions import Questions
from data.api_keys import Api_keys
from data.reqparse_questions import parser
from sqlalchemy import and_

def abort_if_question_not_found(question_id,api_access_key):
    session = db_session.create_session()
    questions = session.query(Questions).filter(and_(Questions.api_access_key==api_access_key,Questions.question_id==question_id)).first()
    session.close()
    if not questions:
        abort(404, message=f"Question {question_id} not found")
def abort_if_api_key_incorrect(api_access_key):
    session = db_session.create_session()
    api_key = session.query(Api_keys).filter(Api_keys.api_key==api_access_key).first()
    session.close()
    if not api_key:
        abort(400,message=f"Api key incorrect")
class QuestionsResource(Resource):
    def get(self,api_access_key,question_id):
        abort_if_api_key_incorrect(api_access_key)
        abort_if_question_not_found(question_id,api_access_key)
        session = db_session.create_session()
        questions = session.query(Questions).filter(and_(Questions.api_access_key==api_access_key,Questions.question_id==question_id)).first()
        session.close()
        return jsonify(
            {'questions': questions.to_dict(only=('question_id','question', 'type', 'answer_options', 'answer',
                                        'owner_id', 'is_public'))})

    def delete(self,api_access_key, question_id):
        abort_if_api_key_incorrect(api_access_key)
        abort_if_question_not_found(question_id,api_access_key)
        session = db_session.create_session()
        questions = session.query(Questions).filter(and_(Questions.api_access_key==api_access_key,Questions.question_id==question_id)).first()
        session.delete(questions)
        session.commit()
        session.close()
        return jsonify({'success': 'OK'})

class QuestionsListResource(Resource):
    def get(self,api_access_key):
        abort_if_api_key_incorrect(api_access_key)
        session = db_session.create_session()
        questions = session.query(Questions).filter(Questions.api_access_key==api_access_key).all()
        session.close()
        return jsonify({'questions': [item.to_dict(only=('question_id','question', 'type', 'answer_options', 'answer',
                                        'owner_id', 'is_public')) for item in questions]})

    def post(self,api_access_key):
        abort_if_api_key_incorrect(api_access_key)
        args = parser.parse_args()
        session = db_session.create_session()
        if session.query(Questions).filter(and_(Questions.question_id==args['question_id'],Questions.api_access_key==api_access_key)).first():
            abort(422, message=f"Question with id {args['question_id']} already in the database")
        questions = Questions(
            question_id = args['question_id'],
            question = args['question'],
            type = args['type'],
            answer_options = args['answer_options'],
            answer = args['answer'],
            owner_id = args['owner_id'],
            is_public = args['is_public'],
            api_access_key = api_access_key
        )
        session.add(questions)
        session.commit()
        session.close()
        return jsonify({'id': args['question_id']})
