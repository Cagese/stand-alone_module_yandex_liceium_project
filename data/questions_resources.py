from flask import jsonify
from flask_restful import Resource, abort

from data import db_session
from data.questions import Questions
from data.reqparse_questions import parser


def abort_if_question_not_found(question_id):
    session = db_session.create_session()
    questions = session.query(Questions).filter(Questions.question_id==question_id).first()
    if not questions:
        abort(404, message=f"Question {question_id} not found")


class QuestionsResource(Resource):
    def get(self, question_id):
        abort_if_question_not_found(question_id)
        session = db_session.create_session()
        questions = session.query(Questions).filter(Questions.question_id==question_id).first()
        return jsonify(
            {'questions': questions.to_dict(only=('question_id','question', 'type', 'answer_options', 'answer',
                                        'owner_id', 'is_public'))})

    def delete(self, question_id):
        abort_if_question_not_found(question_id)
        session = db_session.create_session()
        questions = session.query(Questions).filter(Questions.question_id==question_id).first()
        session.delete(questions)
        session.commit()
        return jsonify({'success': 'OK'})


class QuestionsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        questions = session.query(Questions).all()
        return jsonify({'questions': [item.to_dict(only=('question_id','question', 'type', 'answer_options', 'answer',
                                        'owner_id', 'is_public')) for item in questions]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        if session.query(Questions).filter(Questions.question_id==args['question_id']).first() is not None:
            abort(422, message=f"Question with id {args['question_id']} already in the database")
        questions = Questions(
            question_id = args['question_id'],
            question = args['question'],
            type = args['type'],
            answer_options = args['answer_options'],
            answer = args['answer'],
            owner_id = args['owner_id'],
            is_public = args['is_public']
        )
        session.add(questions)
        session.commit()
        return jsonify({'id': questions.question_id})
